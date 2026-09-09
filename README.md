# CustomBind

A lightweight Python utility for remapping keyboard keys in real time. It is designed for users who want to assign one key to another without changing the game or application itself.

This project is mainly intended for Windows and for use in games or tools that do not provide the desired key bindings.

---

## Features

- Remap one key to another key press
- Store bindings in a simple JSON file
- Add, delete, and reset mappings from an in-app menu
- Log app activity to a text log file
- Quick access to project links from the version menu
- Simple terminal-based interface with colored output

---

## Requirements

- Python 3.9+
- Windows (primary target)
- Access to a terminal or command prompt

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pynput pyautogui colorama
```

---

## Quick Start

From the project folder, run:

```bash
python main.py
```

You can also use the setup helper:

```bash
python setup.py
```

This will prompt whether to install dependencies and then launch the app.

---

## How It Works

When the app starts, it creates a file called `binds.json` if it does not already exist. That file stores the key mappings in this format:

```json
{
    "`": "w",
    "l": "f"
}
```

This means:

- pressing `` (backtick) triggers `w`
- pressing `l` triggers `f`

The app listens for keyboard input globally and, when a mapped key is pressed, it simulates the replacement key press using `pynput` and `pyautogui`.

---

## Main Menu Options

The application starts with a menu like this:

1. Start
2. Edit Binds
3. Version
4. Exit

### 1. Start

Starts the key remapping listener. The program remains active until you stop it manually from the terminal.

### 2. Edit Binds

Lets you:

- add a bind
- delete a bind
- reset all binds
- return to the main menu

### 3. Version

Displays version information and links to the project and community pages.

### 4. Exit

Closes the app.

---

## Configuration

The configuration file is `binds.json` in the project root.

### Default values

If no config file exists, the app creates:

```json
{
    "`": "w",
    "l": "f"
}
```

### Notes

- The project currently supports single-character keys and values.
- Special keys such as `space` are not fully supported in this version.
- Changes are written back to `binds.json` immediately after editing.

---

## Logging

The app saves basic activity to `logs.log`.

Each entry includes:

- app startup information
- bind creation and deletion
- remapping actions
- startup status and menu actions

---

## Important Notes

This program simulates key presses. Depending on the target application or game, some programs may ignore the simulated input or block it because of anti-cheat or input filtering rules.

CustomBind does not modify game files or memory. It is a lightweight, user-controlled utility designed for convenience, not for bypassing protections.

---

## Project Status

This project is currently a personal development tool and is marked as an early alpha build.

The project is active and evolving, and the license and additional polish will be added in future updates.

---

## About

CustomBind is a simple and accessible key remapping tool aimed at making keyboard customization easy and fast.

It is designed to be lightweight, configurable, and easy to run from a terminal without extra setup complexity.

---

## Repository Links

- GitHub: https://github.com/Lunachar1/CustomBind
- Discord: https://discord.com/invite/Hcdkz2KBmR

---

CustomBind — simple key remapping for your setup.