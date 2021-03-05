# fishhook
iaxRpt broadcast

packages<br/>
--------<br/>
python -m venv c:\path\to\myenv<br/>
pip install pywin32<br/>
pip install sounddevice<br/>
pip install SoundFile<br/>
pip install colorama<br/>
pip install pynput<br/>
pip install numpy<br/>
<br/>
usage: fishhook.py [-h] [-f PATH] [-c CHUNK] [-d DELAY] [-l LAG] input_device output_device<br/>
<br/>
positional arguments:<br/>
  input_device   input device<br/>
  output_device  output device<br/>
<br/>
optional arguments:<br/>
  -h, --help     show this help message and exit<br/>
  -f PATH        path to the .wav file (default: tx.wav)<br/>
  -c CHUNK       chunk length (default: 10s)<br/>
  -d DELAY       delay between chunck (default: 5s)<br/>
  -l LAG         ptt lagging (default: 0.5s)<br/>
<br/>
<br/>
<br/>
python window activation<br/>
------------------------<br/>
https://github.com/mhammond/pywin32<br/>
https://stackoverflow.com/questions/2090464/python-window-activation<br/>
<br/>
chunk a list<br/>
------------<br/>
https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks?page=1&tab=votes#tab-top<br/>
