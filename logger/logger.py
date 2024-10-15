from pynput import keyboard
import threading
import os
import subprocess
import sys
import time

ctrl_pressed = False 
space_pressed = False
alt_pressed = False
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(DIR)

ID = 0

def runmenu():
    os.system(f'bash {DIR}/menu')

def runrofi():
    os.system(f'bash {DIR}/rofi')

def on_key_press(key):

    global ctrl_pressed, space_pressed, alt_pressed
    
    try:
        key_id = key.char
    except AttributeError:
        key_id = str(key)
    
    if key_id == 'Key.ctrl':
        ctrl_pressed = True
    elif key_id == 'Key.space':
        space_pressed = True
    elif key_id == 'Key.alt':
        alt_pressed = True
    else:
        ctrl_pressed = False
        space_pressed = False
        alt_pressed = False

    if ctrl_pressed and space_pressed:
        print(ID)
        os.system(f"xdotool windowminimize {ID}")

        if alt_pressed:
            x = threading.Thread(target=runrofi)
        else:
            x = threading.Thread(target=runmenu)
        x.start()
        ctrl_pressed = False
        space_pressed = False
        alt_pressed = False
        time.sleep(1)

def on_key_release(key):
    global ctrl_pressed, space_pressed

    try:
        key_id = key.char
    except AttributeError:
        key_id = str(key)
    
    if key_id == 'Key.ctrl_l':
        ctrl_pressed = False
    elif key_id == 'Key.space':
        space_pressed = False

if __name__ == "__main__":
    # Create a keyboard listener
    title = sys.argv[1]
    ret = subprocess.run(f'wmctrl -l | grep "{title}"', shell=True, capture_output=True, text=True)
    ID = ret.stdout.split(" ")[0]

    print(ID)

    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()


