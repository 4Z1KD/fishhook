from pynput.keyboard import Key, Controller
import time
import win32gui
import sys
import sounddevice as sd
import soundfile as sf
from colorama import init, Fore, Style
import math
import argparse

init()

# Instantiate the parser
parser = argparse.ArgumentParser(description='iaxRpt broadcast')
parser.add_argument('input_device', type=int, help='input device')
parser.add_argument('output_device', type=int, help='output device')
parser.add_argument('-f', metavar='PATH', type=str, help='path to the .wav file (default: %(default)s)', dest="wavfile", default="tx.wav")
parser.add_argument('-c', metavar='CHUNK', type=int, help='chunk length (default: %(default)ss)', dest="chunk_duration", default=10)
parser.add_argument('-d', metavar='DELAY', type=int, help='delay between chunck (default: %(default)ss)', dest="delay", default=5)
parser.add_argument('-l', metavar='LAG', type=float, help='ptt lagging (default: %(default)ss)', dest="ptt_lagging", default=0.5)
args = parser.parse_args()

print("\naudio devices:")
print(sd.query_devices())
sd.default.device = args.input_device,args.output_device

print(f"{Fore.GREEN}file path:\t{args.wavfile}{Style.RESET_ALL}")
print(f"{Fore.GREEN}chunk duration:\t{args.chunk_duration}{Style.RESET_ALL}")
print(f"{Fore.GREEN}delay:\t\t{args.delay}{Style.RESET_ALL}")
print(f"{Fore.GREEN}ptt lagging:\t{args.ptt_lagging}{Style.RESET_ALL}")

# Yield successive n-sized chunks from lst
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

handle = win32gui.FindWindow(None, "iaxRpt")
try:
    if handle:
        # Extract data and sampling rate from a wav file
        data, fs = sf.read(args.wavfile, dtype='float32')
        data_chunks = chunks(data,fs*args.chunk_duration)
        keyboard = Controller()
        win32gui.SetForegroundWindow(handle)        
        i = 0
        for chunk in data_chunks:
            print(f"playing {int(math.ceil(i*args.chunk_duration + len(chunk)/fs))}/{int(math.ceil(len(data)/fs))} sec", end ="\r") 
            i+=1
            keyboard.press(Key.ctrl)
            time.sleep(args.ptt_lagging)
            sd.play(chunk, fs)
            status = sd.wait()  # Wait until file is done playing
            keyboard.release(Key.ctrl)
            time.sleep(args.delay)
    else:
        print(f"{Fore.LIGHTRED_EX}could not find an instance of iaxRpt. did you forget to run it?{Style.RESET_ALL}")
except KeyboardInterrupt:
    print('\nInterrupted by user')
except Exception as e:
    print(type(e).__name__ + ': ' + str(e))