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



# Current app version and welcome screen used on startup.
version = "0.6 ALPHA"

# Show the user name in the startup banner for a more personal welcome.
username = getpass.getuser()
text = f"{Fore.GREEN}Welcome in CustomBind {Fore.BLUE}v{version} {username}!"

# Print the welcome message one character at a time to create a small animated intro.
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.05)

print()
time.sleep(3)
clear()

# Main application loop: redraw the menu after every interaction.
while True:
    clear()

    print(f'{Fore.CYAN}CustomBind v{version}{Style.RESET_ALL}\n')
    tui.opt(["Start","Edit Binds","Version",'Exit'])

    q = input(f"\n{Fore.YELLOW}Select an option: [1-4]{Style.RESET_ALL} ")

    clear()

    if q == "1":
        # Start the global keyboard listener until the user stops the program.
        print(f'{Fore.GREEN}Reset the app to stop the keyboard remmaping')
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
            print(f'{Fore.CYAN}Version {Fore.GREEN}{version}')
            print(f'{Fore.CYAN}M{Fore.GREEN}a{Fore.CYAN}d{Fore.GREEN}e{Fore.CYAN} b{Fore.GREEN}y{Fore.CYAN} L{Fore.GREEN}u{Fore.CYAN}n{Fore.GREEN}a{Fore.CYAN}c{Fore.GREEN}h{Fore.CYAN}a{Fore.GREEN}r')
            print('New updates here:')
            tui.opt(['Open GitHub', 'Join Discord'])
            q4 = input('Select an option betwen 1 and 2 ')
            if q4 == '1':
                webbrowser.open('https://github.com/Lunachar1/CustomBind')
            elif q4 == '2':
                webbrowser.open('https://discord.com/invite/Hcdkz2KBmR')
    elif q == '4':
        # Exit immediately instead of returning to the main menu.
        sys.exit()
    else:
        print('Wrong option! Select number betwen 1 and 5!')
               



    

