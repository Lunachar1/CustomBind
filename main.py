from pynput import keyboard
import pyautogui
import json
import os
import webbrowser
from colorama import Fore, Style
import time
import sys

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

def option(text,nuber):
    return f"{Fore.YELLOW}[{Fore.WHITE}{nuber}{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}"
def gui(options: list):
    for i, text in enumerate(options, 1):
        print(option(text, i))

version = "0.3 BETA"
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'{Fore.CYAN}CustomBind v{version}{Style.RESET_ALL}\n')
    gui(["Start","Edit Binds","Open Github","Watch Tutorial",'Exit'])

    q = input(f"\n{Fore.YELLOW}Select an option: [1-5]{Style.RESET_ALL} ")

    if q == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Reset the app to stop the keyboard remmaping')
        while True:
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
    elif q == '2':
        edit = True
        while edit:
            os.system('cls' if os.name == 'nt' else 'clear')

            for key, value in data.items():
                print(key, ':', value)

            gui(['Add bind', 'Delete bind', 'Reset binds', 'Go to main menu'])

            q2 = input('Select an option: [1-4] ')

            if q2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                for key, value in data.items():
                        print(key, ':', value)

                key = input("Enter the key to bind: ")
                value = input("Enter the key to press: ")

                data[key] = value
                with open("binds.json", "w") as file:
                    json.dump(data, file, indent=4)

            elif q2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                for key, value in data.items():
                    print(key, ':', value)
                q3 = input(f'What bind do you want to delete? [1-{len(data)}] ')
                key = list(data.keys())[int(q3) - 1]
                del data[key]
                with open("binds.json", "w") as file:
                    json.dump(data, file, indent=4)
                

            elif q2 == '3':
                op = input('Are you sure? [Y/N] ')
                if op == 'y' or op == 'Y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    with open("binds.json", "w") as file:
                        json.dump({}, file, indent=4)
                    data = {}
                    print('Binds.json got cleared')
                    time.sleep(2)
                else:
                    pass
            elif q2 == '4':
                edit = False
            else:
                print('Wrong option! Select number betwen 1 and 4!')
    elif q == '3':
        webbrowser.open('https://github.com/Lunachar1/CustomBind')
    elif q == '4':
        print('The tutorial will be recorded when i will reach 1st version (v1.0)')
        time.sleep(2)
    elif q == '5':
        sys.exit()
    else:
        print('Wrong option! Select number betwen 1 and 5!')
               



    

