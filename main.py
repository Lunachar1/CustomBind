from pynput import keyboard
import pyautogui
import json
import os
import webbrowser
from colorama import Fore, Style
import time
import sys
import logs

# Clearing console function for both Windows and Linux.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create the bindings file with defaults the first time the app runs.
if not os.path.exists("binds.json"):
    data = {"`": "w",
            'l':'f'} 

    with open("binds.json", "w") as file:
        json.dump(data, file, indent=4)

with open('binds.json','r') as file:
    data = json.load(file)
logs.log(f'[APP] Loaded {len(data)} bind(s)', include_date=True)

# Convert a configured character into the key object expected by pynput.
def convert_key(key):
    return keyboard.KeyCode.from_char(key)

# Handle each pressed key and send its configured replacement, if any.
def on_press(key):
    try:
        key_name = key.char

        if key_name in data:
            new_key = convert_key(data[key_name])
            pyautogui.press(new_key.char)
            print(f'{Fore.CYAN}[{Fore.BLUE}BIND{Fore.CYAN}]{Fore.WHITE} Successfully reamped {Fore.CYAN}{key.char}{Fore.WHITE} to {Fore.CYAN}{new_key.char}')
            logs.log(f'[BIND] Successfully reamped {key.char} to {new_key.char}')

    except AttributeError:
        # Special keys, such as Shift, do not have a character value.
        pass

# Format one menu entry using the application's terminal colors.
def option(text,nuber):
    return f"{Fore.YELLOW}[{Fore.WHITE}{nuber}{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}"

# Print every option with a human-friendly number starting at one.
def gui(options: list):
    for i, text in enumerate(options, 1):
        print(option(text, i))

version = "0.5 ALPHA"
while True:
    # The main menu is redrawn after every completed action.
    clear()

    print(f'{Fore.CYAN}CustomBind v{version}{Style.RESET_ALL}\n')
    gui(["Start","Edit Binds","Open Github","Watch Tutorial",'Exit'])

    q = input(f"\n{Fore.YELLOW}Select an option: [1-5]{Style.RESET_ALL} ")

    if q == "1":
        # Keep listening until the user stops the program from the terminal.
        clear()
        print(f'{Fore.GREEN}Reset the app to stop the keyboard remmaping')
        logs.log('[APP] Started key remapping')
        while True:
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
    elif q == '2':
        # The bind editor stays open until the user returns to the main menu.
        edit = True
        while edit:
            clear()

            for key, value in data.items():
                print(key, ':', value)

            gui(['Add bind', 'Delete bind', 'Reset binds', 'Go to main menu'])

            q2 = input('Select an option: [1-4] ')

            if q2 == '1':
                # Add a new source-key to replacement-key mapping.
                clear()
                for key, value in data.items():
                        print(key, ':', value)

                key = input("Enter the key to bind: ")
                value = input("Enter the key to press: ")

                data[key] = value
                with open("binds.json", "w") as file:
                    json.dump(data, file, indent=4)
                logs.log(f'[BIND] Added {key} -> {value}')

            elif q2 == '2':
                # Delete the bind selected by its displayed position.
                clear()
                for key, value in data.items():
                    print(key, ':', value)
                q3 = input(f'What bind do you want to delete? [1-{len(data)}] ')
                key = list(data.keys())[int(q3) - 1]
                del data[key]
                with open("binds.json", "w") as file:
                    json.dump(data, file, indent=4)
                logs.log(f'[BIND] Deleted {key}')
                

            elif q2 == '3':
                # Clear every binding only after explicit confirmation.
                op = input('Are you sure? [Y/N] ')
                if op == 'y' or op == 'Y':
                    clear()
                    with open("binds.json", "w") as file:
                        json.dump({}, file, indent=4)
                    data = {}
                    print('Binds.json got cleared')
                    time.sleep(2)
                else:
                    pass
            elif q2 == '4':
                # Leave the editor and let the outer loop redraw the main menu.
                edit = False
            else:
                print('Wrong option! Select number betwen 1 and 4!')
    elif q == '3':
        # Open the project page in the user's default browser.
        webbrowser.open('https://github.com/Lunachar1/CustomBind')
    elif q == '4':
        # This menu item is currently a placeholder for a future tutorial.
        print('The tutorial will be recorded when i will reach 1st version (v1.0)')
        time.sleep(2)
    elif q == '5':
        # Exit immediately instead of returning to the main menu.
        sys.exit()
    else:
        print('Wrong option! Select number betwen 1 and 5!')
               



    

