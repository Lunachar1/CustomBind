from pynput import keyboard
import pyautogui
import json
import os
import webbrowser


if not os.path.exists("binds.json"):
    data = {"`": "w",
            'l':'f'} 

    with open("binds.json", "w") as file:
        json.dump(data, file, indent=4)

with open('binds.json','r') as file:
    data = json.load(file)

def convert_key(key):
    return keyboard.KeyCode.from_char(key)

def on_press(key):
    try:
        key_name = key.char

        if key_name in data:
            new_key = convert_key(data[key_name])
            pyautogui.press(new_key.char)

    except AttributeError:
        pass


print('CustomBind v0.1\n')
q = input('Do you know how to change binds? [Y/N] ')
if q == 'y' or q == 'Y':
    q1 = input('Do you want to start the Key Remapping? [Y/N]')
    if q1 == 'Y' or q1 == 'y':
        while True:
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
    else:
        pass
else:
    webbrowser.open('google.com')