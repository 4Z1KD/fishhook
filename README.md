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
fishhook expects up to 8 parameters:
input_device_id     input device id (fishhook.py -a for list of devices)
output_device_id    output device id (fishhook.py -a for list of devices)
-f PATH             path to the .wav file (default: tx.wav)
-c CHUNK            chunk length (default: 10s)
-d DELAY            delay between chunck (default: 5s)
-l LAG              ptt lagging (default: 0.5s)
-s COM[n]           serial port
--realptt           trigger a physical PTT over the serial port

help
-----
python fishhook.py -h

</pre>
