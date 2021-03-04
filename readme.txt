packages
--------
python -m venv c:\path\to\myenv
pip install pywin32
pip install sounddevice
pip install SoundFile
pip install colorama
pip install pynput

usage
-----
fishhook.py expects 4 parameters:
file_path - a path to a .wav file
chunk_duration - the size of each chunk of the wav file to be played (in seconds) - default is 60
delay - the time to wait between chunks (in seconds) - default is 5
ptt_lagging - the time to wait between pressing the ptt and playing the chunk (in seconds) - default is 0.5



python window activation
------------------------
https://github.com/mhammond/pywin32
https://stackoverflow.com/questions/2090464/python-window-activation

chunk a list
------------
https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks?page=1&tab=votes#tab-top

