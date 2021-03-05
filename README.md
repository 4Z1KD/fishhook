# fishhook ![alt text](https://raw.githubusercontent.com/4Z1KD/fishhook/main/fishhook48.png)

this small script allows iaxRpt client users to semi-automate their broadcast system.<br>
it emulates the 'Ctrl' keypress that iaxRpt uses to activate the ptt.<br>
it also splices the input .wav file to a fixed-size chunks so that it does not
exceed the local repeater timeout timer.<br>
a delay between chunks can also configured.<br>
a serial COM port may be set, if one wants to use a physical PTT.<br>
finally, the user can redirect the audio through different audio devices.<br>
<br>
#installation 🎣
---------------<br>
create a virtual env: python -m venv c:\path_to_myenv<br>
add c:\path_to_myenv\Scripts to your system PATH<br>
activate<br>
pip install pywin32<br>
pip install sounddevice<br>
pip install SoundFile<br>
pip install colorama<br>
pip install pynput<br>
pip install numpy<br>
download and unzip fishhook<br>
<br>
#usage 🎣
--------<br>
The best way is to use init_fishhook.bat - it contains all the required parameters.<br>
one thing to pay attention to - select the correct input and output audio device id.<br>
to get the list of devices, run: fishhook.py -a<br>
<br>
fishhook expects up to 8 parameters:<br>
input_device_id     input device id (fishhook.py -a for list of devices)<br>
output_device_id    output device id (fishhook.py -a for list of devices)<br>
-f PATH             path to the .wav file (default: tx.wav)<br>
-c CHUNK            chunk length (default: 10s)<br>
-d DELAY            delay between chunck (default: 5s)<br>
-l LAG              ptt lagging (default: 0.5s)<br>
-s COM[n]           serial port<br>
--realptt           trigger a physical PTT over the serial port<br>
<br>
#help 🎣
-----<br>
python fishhook.py -h<br>
