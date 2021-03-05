# fishhook
<pre>
this small script allows iaxRpt client users to semi-automate their broadcast system.
it emulates the 'Ctrl' keypress that iaxRpt uses to activate the ptt.
it also splices the input .wav file to a fixed-size chunks so that it does not exceed the local repeater timeout timer.
a delay between chunks can also configured.
a serial COM port may be set, if one wants to use a physical PTT.
finally, the user can redirect the audio through different audio devices.
</pre>
<p/>
<pre>
installation
---------------
python -m venv c:\path_to_myenv
cd c:\path_to_myenv
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
