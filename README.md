# ⌨️ CustomBind

<p align="center">
  <strong>A small keyboard remapping tool for Windows.</strong>
</p>

<p align="center">
  Remap keys • Save bindings • Edit configuration • Run from the terminal
</p>

<div align="center">
  <img src="https://img.shields.io/badge/version-0.7%20ALPHA-2f855a?style=flat-square" alt="Version 0.7 ALPHA">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python 3.9 or newer">
  <img src="https://img.shields.io/badge/platform-Windows-0078D4?style=flat-square&amp;logo=windows&amp;logoColor=white" alt="Windows platform">
  <img src="https://img.shields.io/badge/status-early%20development-c05621?style=flat-square" alt="Early development">
  <br>
  <img src="https://img.shields.io/github/stars/Lunachar1/CustomBind?style=flat-square" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/Lunachar1/CustomBind?style=flat-square" alt="GitHub forks">
  <img src="https://img.shields.io/github/issues/Lunachar1/CustomBind?style=flat-square" alt="GitHub issues">
</div>

---

## ✨ What is CustomBind?

**CustomBind** is a Python program that remaps selected keyboard keys while it is running.

It can be useful when a game or application does not have the key binding you need.

CustomBind listens for keyboard input and sends the replacement key from your configuration. It does not change the target application.

> **Example:**
> Press `L` → CustomBind sends `F`

The project is designed for **Windows** and runs in a terminal.

---

## 🚀 Features

* ⌨️ Real-time keyboard remapping
* 🔄 Map one key to another
* 💾 Store bindings in `binds.json`
* ➕ Add new bindings from the application
* 🗑️ Delete existing bindings
* ♻️ Reset all bindings
* 📝 Activity logging
* 🎨 Colored terminal interface
* 📦 Simple Python-based setup
* 🔗 Quick access to project/community links
* 🪶 Runs locally from Python

---

## 📊 Project Status

**Current version: `0.7 ALPHA`**

CustomBind is an early development project.

Basic remapping and bind management are working. Some keyboard keys are not supported yet, and the project may change in future releases.

### Development status

| Feature                      | Status |
| ---------------------------- | :----: |
| Basic key remapping          |    ✅   |
| JSON configuration           |    ✅   |
| Add bindings                 |    ✅   |
| Delete bindings              |    ✅   |
| Reset bindings               |    ✅   |
| Activity logging             |    ✅   |
| Terminal interface           |    ✅   |
| Windows support              |    ✅   |
| Standalone `.exe`            |   🚧   |
| Installer                    |   🚧   |
| Extended special-key support |   🚧   |
| Advanced configuration       |   📋   |

---

## 💻 Requirements

### Supported platform

* Windows 10 / 11
* Python 3.9+

### Dependencies

CustomBind currently uses:

* `pynput`
* `pyautogui`
* `colorama`

---

## 📥 Installation

### Option 1 — Run from source

Clone the repository:

```bash
git clone https://github.com/Lunachar1/CustomBind.git
cd CustomBind
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r req.txt
```

Start CustomBind:

```powershell
python main.py
```

---

### Option 2 — Setup helper

CustomBind also includes a setup helper:

```powershell
python setup.py
```

The setup script installs the dependencies from `req.txt` and then starts the application.

---

### Option 3 — Windows executable

A standalone Windows build is not available yet. It may be added to the **GitHub Releases** section later.

Planned format:

```text
CustomBind-x.x.x-Windows.exe
```

This would allow CustomBind to run without a separate Python installation.

---

## ⚡ Quick Start

After starting the application:

```text
CustomBind v0.7 ALPHA

1. Start
2. Edit Binds
3. Version
4. Exit
```

Choose **Start** to activate the keyboard listener.

For example, with:

```json
{
    "`": "w",
    "l": "f"
}
```

the application behaves like:

```text
` → W
L → F
```

Press `Esc` to stop the listener and return to the main menu.

---

## ⚙️ Configuration

CustomBind stores keyboard mappings in:

```text
binds.json
```

### Example

```json
{
    "`": "w",
    "l": "f"
}
```

This means:

| Input   | Output |
| ------- | ------ |
| `` ` `` | `W`    |
| `L`     | `F`    |

Bindings can be edited directly in the JSON file or through the application's **Edit Binds** menu.

### Current limitations

At the moment:

* Single-character keys are primarily supported.
* Some special keys are not fully supported.
* Modifier combinations such as `Ctrl + Key` are not currently part of the main binding system.
* Support for additional keyboard keys is planned.

---

## 🖥️ Main Menu

### `1. Start`

Starts the keyboard remapping listener.

Press:

```text
Esc
```

to stop the listener and return to the main menu.

### `2. Edit Binds`

Allows you to:

* Add a binding
* Delete a binding
* Reset all bindings
* Return to the main menu

### `3. Version`

Displays:

* Current CustomBind version
* Project information
* Repository links
* Community links

### `4. Exit`

Closes the application.

---

## 📝 Logging

CustomBind records basic application activity in:

```text
logs.log
```

Logs can contain information such as:

* Application startup
* Menu actions
* Binding creation
* Binding deletion
* Remapping activity
* Application status

Example:

```text
[APP] CustomBind started
[APP] Loaded 2 bind(s)
[APP] Added bind: l -> f
```

---

## 🔒 Safety & Compatibility

CustomBind does **not** modify game files or application memory.

It works by listening for keyboard input and simulating keyboard presses.

Some applications may:

* Ignore simulated input
* Use their own input systems
* Restrict external keyboard input
* Block simulated input
* Behave differently when input is generated programmatically

Compatibility therefore depends on the target application.

CustomBind is intended as a **general-purpose keyboard utility**, not as a tool for bypassing security or anti-cheat protections.

---

## 📁 Project Structure

```text
CustomBind/
│
├── main.py
├── setup.py
├── req.txt
├── binds.json
├── logs.log
├── README.md
├── .gitignore
│
├── venv/                 # Local virtual environment
│
└── ...
```

> `venv/` should remain local and should **not** be committed to Git.

---

## 🗺️ Roadmap

### `v0.7 ALPHA` — Current

* [x] Basic remapping
* [x] JSON configuration
* [x] Bind management
* [x] Logging
* [x] Terminal interface

### Future releases

* [ ] More special-key support
* [ ] Modifier combinations
* [ ] Improved configuration system
* [ ] Better error handling
* [ ] Improved terminal UI
* [ ] Standalone Windows `.exe`
* [ ] Windows installer
* [ ] Automatic updates
* [ ] More configuration options
* [ ] Improved documentation

---

## 🐛 Bug Reports & Suggestions

Found a bug or have an idea?

Open an **Issue** on GitHub and include:

1. CustomBind version
2. Windows version
3. What you were trying to do
4. What happened
5. Any relevant error message

For bugs, including the relevant part of `logs.log` can also help.

---

## 🤝 Contributing

CustomBind is a personal development project.

Contributions, bug reports, suggestions and improvements are welcome.

Before submitting a large change, it is recommended to open an issue first so the idea can be discussed.

---

## 📈 GitHub

<p align="center">

⭐ If you use the project, feedback and bug reports are welcome.

</p>

Repository:

https://github.com/Lunachar1/CustomBind

Community:

https://discord.com/invite/Hcdkz2KBmR

---

## 📜 License

A formal license will be added in a future release.

Until then, please treat the repository as an **early-stage development project** and do not redistribute modified versions as official CustomBind releases.

---

<p align="center">

### ⌨️ CustomBind

**Keyboard remapping from the terminal.**

`0.7 ALPHA`

</p>
