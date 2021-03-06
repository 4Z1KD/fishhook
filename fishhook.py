from pynput.keyboard import Key, Controller
import time
from serial.serialutil import SerialException
import win32gui
import sounddevice as sd
import soundfile as sf
from colorama import init, Fore, Style
import math
import argparse
import serial

init()

# Instantiate the parser
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-a', '--list-devices', action='store_true', help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print("\naudio devices:")
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(description='iaxRpt broadcast', formatter_class=argparse.RawDescriptionHelpFormatter, parents=[parser])
parser.add_argument('input_device_id', type=int, help='input device id (fishhook.py -a for list of devices)')
parser.add_argument('output_device_id', type=int, help='output device id (fishhook.py -a for list of devices)')
parser.add_argument('-f', metavar='FILE_PATH', type=str, help='path to the .wav file (default: %(default)s)', dest="wavfile", default="tx.wav")
parser.add_argument('-c', metavar='CHUNK_DURATION', type=int, help='chunk length (default: %(default)ss)', dest="chunk_duration", default=10)
parser.add_argument('-d', metavar='DELAY', type=int, help='delay between chunck (default: %(default)ss)', dest="delay", default=5)
parser.add_argument('-l', metavar='LAG', type=float, help='ptt lagging (default: %(default)ss)', dest="ptt_lagging", default=0.5)
parser.add_argument('-s', metavar='COM[n]', nargs='?', type=str, help='serial port', dest="serial_port")
parser.add_argument('-mode', type=str.upper, help='PTT for physical ptt, IAXRPT from iaxRpt client', dest="mode", default="IAXRPT", choices=["PTT", "IAXRPT", "DUDE"])
args = parser.parse_args(remaining)

sd.default.device = args.input_device_id,args.output_device_id

print(f"{Fore.GREEN}file path:\t{args.wavfile}{Style.RESET_ALL}")
print(f"{Fore.GREEN}chunk duration:\t{args.chunk_duration}{Style.RESET_ALL}")
print(f"{Fore.GREEN}delay:\t\t{args.delay}{Style.RESET_ALL}")
print(f"{Fore.GREEN}ptt lagging:\t{args.ptt_lagging}{Style.RESET_ALL}")
print(f"{Fore.GREEN}COM port:\t{args.serial_port}{Style.RESET_ALL}")
print(f"{Fore.GREEN}mode:\t{args.mode}{Style.RESET_ALL}")

physical_port = False
iaxrpt_client = False
dude_client = False

if args.mode.upper() == "PTT":
    if args.serial_port:
        try:
            ser = serial.Serial(args.serial_port)
            ser.setRTS(False)
            physical_port = True
        except SerialException:
            physical_port = False
            print(f"{Fore.YELLOW}failed to open '{args.serial_port}'. check device manager for the correct port.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}ptt mode was selected but no COM port was set.{Style.RESET_ALL}")
elif args.mode.upper() == "IAXRPT":
    handle = win32gui.FindWindow(None, "iaxRpt")
    if handle:
        win32gui.SetForegroundWindow(handle)
        iaxrpt_client = True
    else:
        iaxrpt_client = False
        print(f"{Fore.YELLOW}could not find an instance of iaxRpt. did you forget to run it?{Style.RESET_ALL}")
elif args.mode.upper() == "DUDE":
    handle = win32gui.FindWindow(None, "DUDE-Star")
    if handle:
        win32gui.SetForegroundWindow(handle)
        dude_client = True
    else:
        dude_client = False
        print(f"{Fore.YELLOW}could not find an instance of DUDE-Star. did you forget to run it?{Style.RESET_ALL}")

# print(f"Modes:")
# print(f"{Fore.GREEN}PTT:\t{physical_port}{Style.RESET_ALL}")
# print(f"{Fore.GREEN}IAXRPT:\t{iaxrpt_client}{Style.RESET_ALL}")
# print(f"{Fore.GREEN}DUDE:\t{dude_client}{Style.RESET_ALL}")

# Yield successive n-sized chunks from lst
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

try:
    if physical_port or iaxrpt_client or dude_client:
        # Extract data and sampling rate from a wav file
        data, fs = sf.read(args.wavfile, dtype='float32')
        data_chunks = chunks(data,fs*args.chunk_duration)
        keyboard = Controller()    
        i = 0
        for chunk in data_chunks:
            print(f"playing {int(math.ceil(i*args.chunk_duration + len(chunk)/fs))}/{int(math.ceil(len(data)/fs))} sec", end ="\r") 
            i+=1

            if physical_port:
                ser.setRTS(True)
            elif iaxrpt_client:
                keyboard.press(Key.ctrl)
            elif dude_client:
                keyboard.press(Key.space)

            time.sleep(args.ptt_lagging)
            sd.play(chunk, fs)
            status = sd.wait()  # Wait until file is done playing

            if dude_client:
                keyboard.release(Key.space)
            elif iaxrpt_client:
                keyboard.release(Key.ctrl)
            elif physical_port:
                ser.setRTS(False)

            time.sleep(args.delay)
    #else:
        #print(f"{Fore.LIGHTRED_EX}both physical interface and iaxRpt are not available{Style.RESET_ALL}")
    
except KeyboardInterrupt:
    print('\nInterrupted by user')
except Exception as e:
    print(type(e).__name__ + ': ' + str(e))