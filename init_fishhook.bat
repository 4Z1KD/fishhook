@echo off
REM start cmd /k "activate & cd /d C:\Users\Gil\Documents\Projects\fishhook & python fishhook.py -h & python fishhook.py -a
set FILE_NAME=tx.wav
set /A CHUNK_DURATION=40
set /A DELAY=5
set /A PTT_LAG=0.5
set /A INPUT_DEVICE_ID=2
set /A OUTPUT_DEVICE_ID=10

start cmd /k "activate & cd /d C:\Users\Gil\Documents\Projects\fishhook & python fishhook.py -f %FILE_NAME% -c %CHUNK_DURATION% -d %DELAY% -l %PTT_LAG% %INPUT_DEVICE_ID% %OUTPUT_DEVICE_ID%"
exit
