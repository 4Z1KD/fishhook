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
<br/>
usage<br/>
-----<br/>
fishhook.py expects 4 parameters:<br/>
file_path - a path to a .wav file<br/>
chunk_duration - the size of each chunk of the wav file to be played (in seconds) - default is 60<br/>
delay - the time to wait between chunks (in seconds) - default is 5<br/>
ptt_lagging - the time to wait between pressing the ptt and playing the chunk (in seconds) - default is 0.5<br/>
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
