from pynput import keyboard
import pyautogui
import json
import os
import webbrowser
from colorama import Fore, Style
import time
import sys
import utilities.logs as logs
import utilities.tui as tui
import getpass


# Clear the terminal so the menu redraws cleanly on each loop.
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
    if key == keyboard.Key.esc:
        return False

    try:
        key_name = key.char

        if key_name in data:
            new_key = convert_key(data[key_name])
            pyautogui.press(new_key.char)
            print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}BIND{Fore.LIGHTCYAN_EX}]{Fore.WHITE} Successfully reamped {Fore.LIGHTYELLOW_EX}{key.char}{Fore.WHITE} to {Fore.LIGHTYELLOW_EX}{new_key.char}')
            logs.log(f'[BIND] Successfully reamped {key.char} to {new_key.char}')

    except AttributeError:
        # Special keys, such as Shift, do not have a character value.
        pass



# Current app version and welcome screen used on startup.
version = "0.7.1 ALPHA"

# Show the user name in the startup banner for a more personal welcome.
username = getpass.getuser()
text = f"{Fore.LIGHTGREEN_EX}Welcome in CustomBind {Fore.LIGHTCYAN_EX}v{version} {username}!"

clear()

# Print the welcome message one character at a time to create a small animated intro.
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.05)


print()
time.sleep(2)
clear()

# Main application loop: redraw the menu after every interaction.
while True:
    clear()

    print(f'{Fore.LIGHTCYAN_EX}CustomBind v{version}{Style.RESET_ALL}\n')
    tui.opt(["Start","Edit Binds","Version",'Exit'])

    q = input(f"\n{Fore.LIGHTYELLOW_EX}Select an option: [1-4]{Style.RESET_ALL} ")

    clear()

    if q == "1":
        # Start the global keyboard listener until the user stops the program.
        print(f'{Fore.LIGHTGREEN_EX}Press {Fore.LIGHTRED_EX}ESC{Fore.LIGHTGREEN_EX} to stop the keyboard remmaping')
        logs.log('[APP] Started key remapping')
        while True:
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
    elif q == '2':
        # Open the binding editor and keep it open until the user exits back to the menu.
        edit = True
        while edit:
            clear()

            for key, value in data.items():
                print(key, ':', value)

            tui.opt(['Add bind', 'Delete bind', 'Reset binds', 'Go to main menu'])

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
        # Display version information and quick links to the project and community.
        version_gui = True
        while version_gui:
            clear()
            print(f'{Fore.LIGHTCYAN_EX}Version {Fore.LIGHTGREEN_EX}{version}')
            print(f'{Fore.LIGHTCYAN_EX}M{Fore.LIGHTGREEN_EX}a{Fore.LIGHTCYAN_EX}d{Fore.LIGHTGREEN_EX}e{Fore.LIGHTCYAN_EX} b{Fore.LIGHTGREEN_EX}y{Fore.LIGHTCYAN_EX} L{Fore.LIGHTGREEN_EX}u{Fore.LIGHTCYAN_EX}n{Fore.LIGHTGREEN_EX}a{Fore.LIGHTCYAN_EX}c{Fore.LIGHTGREEN_EX}h{Fore.LIGHTCYAN_EX}a{Fore.LIGHTGREEN_EX}r')
            print('New updates here:')
            tui.opt(['Open GitHub', 'Join Discord', 'Open Website'])
            q4 = input('Select an option betwen 1 and 3 ')
            if q4 == '1':
                webbrowser.open('https://github.com/Lunachar1/CustomBind')
                version_gui = False
            elif q4 == '2':
                webbrowser.open('https://discord.com/invite/Hcdkz2KBmR')
                version_gui = False
            elif q4 == '3':
                webbrowser.open('https://lunachar.onrender.com')
                version_gui = False
    elif q == '4':
        # Exit immediately instead of returning to the main menu.
        sys.exit()
    else:
        print('Wrong option! Select number betwen 1 and 5!')
               



    

