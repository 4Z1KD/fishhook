# fishhook ![alt text](https://raw.githubusercontent.com/4Z1KD/fishhook/main/fishhook48.png)

this small script supports broadcating an audio file through 2 different paths: external client or physical PTT<br>
if iaxRpt client is selected, it emulates the 'Ctrl' keypress to activate the ptt.<br>
if DUDE-Star client is selected, it emulates the 'Space' keypress to activate the ptt.<br>
it also splices the input .wav file to a fixed-size chunks so that it does not
exceed the local repeater timeout timer.<br>
a delay between chunks can also configured.<br>
a serial COM port may be set, if one wants to use a physical PTT.<br>
finally, the user can redirect the audio through different audio devices.<br>
<br>
# installation 🎣<br>
create a virtual env: python -m venv c:\path_to_myenv<br>
add c:\path_to_myenv\Scripts to your system PATH<br>
activate<br>
pip install pywin32<br>
pip install sounddevice<br>
pip install SoundFile<br>
pip install colorama<br>
pip install pynput<br>
pip install pyserial<br>
pip install numpy<br>
download and unzip fishhook<br>
<br>
# usage 🎣<br>
The best way is to use init_fishhook.bat - it contains all the required parameters.<br>
one thing to pay attention to - select the correct input and output audio device id.<br>
to get the list of devices, run: fishhook.py -a<br>
<br>
fishhook expects up to 8 parameters:<br>
<table>
  <tr><td>input_device_id</td><td>input device id (fishhook.py -a for list of devices)</td></tr>
  <tr><td>output_device_id</td><td>output device id (fishhook.py -a for list of devices)</td></tr>
  <tr><td>-f PATH</td><td>path to the .wav file (default: tx.wav)</td></tr>
  <tr><td>-c CHUNK</td><td>chunk length (default: 10s)</td></tr>
  <tr><td>-d DELAY</td><td>delay between chunck (default: 5s)</td></tr>
  <tr><td>-l LAG</td><td>ptt lagging (default: 0.5s)</td></tr>
  <tr><td>-s COM[n]</td><td>serial port</td></tr>
  <tr><td>-mode</td><td>choose between physical PTT / iaxRpt client / DUDE-Star client</td></tr>
</table>
<br>

# help🎣<br>
python fishhook.py -h<br>
