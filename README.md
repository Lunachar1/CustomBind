# CustomBind

> A simple and lightweight key remapping tool for games and applications.

CustomBind allows you to remap keyboard keys in games and applications that do not provide built-in key binding customization.

The program detects when a specific key is pressed and automatically sends another key instead.

For example:

```text
` → W
L → F
```

Pressing `` ` `` will automatically send `W`.

---

## ✨ Features

- 🔄 **Key Remapping** — remap one keyboard key to another.
- ⚡ **Real-Time Input** — remapped keys are sent immediately.
- 📄 **JSON Configuration** — store your key bindings in a simple `binds.json` file.
- 🛠️ **Easy Configuration** — change bindings without modifying the Python source code.
- 📁 **Automatic Configuration** — `binds.json` is automatically created if it does not exist.
- 🐍 **Python-Based** — built with Python using lightweight libraries.

---

## 📋 Requirements

- Python 3.x
- Windows
- [pynput](https://pypi.org/project/pynput/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)

### Installation

Install the required Python packages:

```bash
pip install pynput pyautogui
```

---

## ⚙️ Configuration

CustomBind uses a `binds.json` file to store key mappings.

If the file does not exist, CustomBind automatically creates it with the default configuration:

```json
{
    "`": "w",
    "l": "f"
}
```

The **key on the left** is the key you press.

The **key on the right** is the key that CustomBind sends.

### Example

```json
{
    "q": "e",
    "f": "r",
    "l": "space"
}
```

This configuration means:

```text
Q → E
F → R
L → SPACE
```

---

## 🔧 How It Works

CustomBind listens for keyboard input using `pynput`.

When a key is pressed, the program:

```text
Keyboard Input
      ↓
    pynput
      ↓
Check binds.json
      ↓
Find mapped key
      ↓
   PyAutoGUI
      ↓
Send replacement key
```

### Example

If `binds.json` contains:

```json
{
    "`": "w"
}
```

and the user presses `` ` ``:

```text
Press `
   ↓
pynput detects `
   ↓
CustomBind checks binds.json
   ↓
Finds "`": "w"
   ↓
PyAutoGUI sends W
```

---

## 🚀 Usage

Run the program with:

```bash
python main.py
```

You will be asked:

```text
CustomBind v0.1

Do you know how to change binds? [Y/N]
```

If you already know how to edit `binds.json`, enter:

```text
Y
```

You will then be asked:

```text
Do you want to start the Key Remapping? [Y/N]
```

Enter `Y` to start the key remapper.

If you answer `N` to the first question, CustomBind will open a web browser with information about changing the bindings.

---

## 📁 Project Structure

```text
CustomBind/
│
├── main.py
├── binds.json
└── README.md
```

### `main.py`

Contains the main CustomBind application.

### `binds.json`

Contains the user's custom key mappings.

### `README.md`

Contains the project documentation.

---

## 🗺️ Roadmap

### v0.1

- [x] Basic key remapping
- [x] JSON-based configuration
- [x] Automatic `binds.json` creation
- [x] Real-time keyboard detection
- [x] Basic user setup

### Future

- [ ] Graphical User Interface (GUI)
- [ ] Add, edit and remove bindings directly from the application
- [ ] Support special keys such as `Space`, `Enter`, `Shift`, `Ctrl`, etc.
- [ ] Mouse button remapping
- [ ] Multiple configuration profiles
- [ ] Game-specific profiles
- [ ] Automatic profile switching
- [ ] Enable/disable remapping with a hotkey
- [ ] Configuration validation
- [ ] Better error handling
- [ ] Standalone `.exe` release
- [ ] Improved input handling
- [ ] Customizable application settings

---

## ⚠️ Limitations

CustomBind is currently an **early prototype**.

Some games or applications may not accept simulated keyboard input.

Games using certain anti-cheat systems may also block or restrict applications that generate simulated keyboard input.

CustomBind does not modify game files or game memory.

---

## 🔒 Safety

CustomBind is designed to operate externally by listening for keyboard input and sending replacement keyboard input.

It does not modify the game's files or memory.

Users should always check the rules and terms of service of the games they use CustomBind with.

---

## 📜 License

This project is currently a personal development project.

The license will be added in a future release.

---

## ⭐ About

**CustomBind** is a small project focused on providing simple and accessible key remapping for games and applications.

The goal is to make key remapping easy, lightweight and configurable without requiring changes to the application or game itself.

---

**CustomBind — Simple Key Remapping.**