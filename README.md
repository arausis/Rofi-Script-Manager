This is a basic script manager. It uses rofi to display and automatically run a series of custom scripts. A few basic scripts are incldued here, but any script can be added by simply creating a new file in the main project directory. 

The logger directory included a basic bash and python script combination which will log keys systemwide, opening the script menu on a key press, and opening a navitation window on a seperate key press.
The default keys are 'Space + ctrl' and 'Space + alt + ctrl' respectively.

It should be noted that this project only runs in linux, and requires rofi, python, qualculate and xdotool to run. 
xdotool is only required to minimize the python window, and can be removed from the dependencies by deleting a few lines from logger.py
qualculate is only required for the calculate script

This project is by no means meant to be a fully bundled application, it is just a personal efficiency script that I want to share with a few like-minded friends.

You might want to add the logger bash script to your startup, and the script will run seamlessly

[[Demo]](https://www.youtube.com/embed/GfpqhAMpxkI?si=UbtgFxvPUiejD3RV)
