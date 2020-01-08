# Local Switch off after idle time of specified time is reached.
Make sure the idleTime module is made global and the run.py script is used as a startup program.

You can also use run.exe in your startup folder


Edit run.py to set the time to 15 mins or less than screen time to avoid going into sleep or to avoid early shutdown.
If you want a new bundle, make the new bundle without the prompt by renaming the run.py file to run.pyw and use pyinstaller.
