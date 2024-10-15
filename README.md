This is a basic script manager. It uses rofi to display and automatically run a series of custom scripts. A few basic scripts are incldued here, but any script can be added by simply creating a new file in the main project directory. 

The logger directory included a basic bash and python script combination which will logg keys systemwide, opening the script menu on a a key press, and opening a navitation window on a seperate key press.
The default keys are 'Space + ctrl' and 'Space + alt + ctrl' respectively.

It should be noted that this project only runs in linux, and requires rofi, python, and xdotool to run. 
xdotool is only required to minimize the python window, and can be removed from the dependencies by deleting a few lines from logger.py
