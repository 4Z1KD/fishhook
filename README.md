# fishhook
iaxRpt broadcast

<pre>
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
fishhook expects 6 parameters:
input_device_id        input device
output_device_id       output device
-f PATH             path to the .wav file (default: tx.wav)
-c CHUNK            chunk length (default: 10s)
-d DELAY            delay between chunck (default: 5s)
-l LAG              ptt lagging (default: 0.5s)

help
-----
fishhook.py -h

</pre>
