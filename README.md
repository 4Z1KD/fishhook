# fishhook
iaxRpt broadcast

<block>
installation
---------------
python -m venv c:\path\to\myenv
cd c:\path\to\myenv
activate
pip install pywin32
pip install sounddevice
pip install SoundFile
pip install colorama
pip install pynput
pip install numpy

usage
--------
fishhook.py expects 6 parameters:
input_deviceinput device
output_device   output device
-f PATH   path to the .wav file (default: tx.wav)
-c CHUNK    chunk length (default: 10s)
-d DELAY    delay between chunck (default: 5s)
-l LAG    ptt lagging (default: 0.5s)
</block>
