from colorama import Fore, Style
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTCYAN_EX

# Format one menu item so it appears with a colored number and label.
def option(text, nuber):
    return f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTCYAN_EX}{nuber}{Fore.LIGHTYELLOW_EX}] {Fore.WHITE}{text}{Style.RESET_ALL}"


# Print a numbered list of menu choices to the terminal.
def opt(options: list):
    for i, text in enumerate(options, 1):
        print(option(text, i))