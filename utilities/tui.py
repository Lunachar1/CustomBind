from colorama import Fore, Style


# Format one menu item so it appears with a colored number and label.
def option(text, nuber):
    return f"{Fore.YELLOW}[{Fore.WHITE}{nuber}{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}"


# Print a numbered list of menu choices to the terminal.
def opt(options: list):
    for i, text in enumerate(options, 1):
        print(option(text, i))