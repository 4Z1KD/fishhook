from pynput.keyboard import Key, Controller
import time
import win32gui
import sys
import sounddevice as sd
import soundfile as sf
from colorama import init, Fore, Style
init()

chunk_duration = 60
delay = 5
ptt_lagging = 0.5

try:
    wavfile = sys.argv[1]
except:
    print(f"{Fore.RED}file path not specified")
    sys.exit(1)
try:
    chunk_duration = int(sys.argv[2])
except:
    print(f"{Fore.RED}wrong chunk duration. {Fore.YELLOW}using default [{chunk_duration}]{Style.RESET_ALL}")
    #sys.exit(2)
try:
    delay = float(sys.argv[3])
except:
    print(f"{Fore.RED}wrong chunk delay. {Fore.YELLOW}using default [{delay}]{Style.RESET_ALL}")
    #sys.exit(3)
try:
    ptt_lagging = float(sys.argv[4])
except:
    print(f"{Fore.RED}wrong ptt lagging. {Fore.YELLOW}using default [{ptt_lagging}]{Style.RESET_ALL}")
    #sys.exit(4)

print(f"{Fore.GREEN}file path:\t{wavfile}{Style.RESET_ALL}")
print(f"{Fore.GREEN}chunk duration:\t{chunk_duration}{Style.RESET_ALL}")
print(f"{Fore.GREEN}delay:\t\t{delay}{Style.RESET_ALL}")
print(f"{Fore.GREEN}ptt lagging:\t{ptt_lagging}{Style.RESET_ALL}")

# Yield successive n-sized chunks from lst
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

handle = win32gui.FindWindow(None, "iaxRpt")
if handle:
    # Extract data and sampling rate from a wav file
    try:
        data, fs = sf.read(wavfile, dtype='float32')
    except:
        print(f"{Fore.RED}WAV file not found: {Fore.YELLOW}[{wavfile}]{Style.RESET_ALL}")
        sys.exit(5)
    data_chunks = chunks(data,fs*chunk_duration)
    win32gui.SetForegroundWindow(handle)
    keyboard = Controller()

    for chunk in data_chunks:
        keyboard.press(Key.ctrl)
        time.sleep(ptt_lagging)
        sd.play(chunk, fs)
        status = sd.wait()  # Wait until file is done playing
        keyboard.release(Key.ctrl)
        time.sleep(delay)
else:
    print(f"{Fore.LIGHTRED_EX}could not find an instance of iaxRpt. did you forget to run it?{Style.RESET_ALL}")