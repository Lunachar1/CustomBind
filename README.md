# CustomBind

CustomBind is a small Python program for remapping keyboard keys. When you press a key that has a binding, it sends the replacement key instead.

It is mainly intended for Windows and for games or applications that do not have the key binding you need.

## Requirements

- Windows
- Python 3

Install the required packages from the project folder:

```bash
pip install pynput pyautogui colorama
```

## Run it

```bash
python main.py
```

The program opens a simple menu. Choose `Start` to begin remapping, or choose `Edit Binds` to add and delete bindings from the menu.

Choose `Exit` to leave the menu. While remapping is running, stop the program with `Ctrl+C` in the terminal or by closing the terminal window.

## Bindings

Bindings are stored in `binds.json`. The key on the left is the key to listen for, and the value is the key to send:

```json
{
    "`": "w",
    "l": "f"
}
```

If `binds.json` does not exist, the program creates it with these default bindings. The current version is intended for single-character keys and values, so names such as `space` are not supported as special keys.

## Notes

The program listens for keyboard input globally and sends simulated key presses using `pynput` and `PyAutoGUI`. Some games or applications may ignore simulated input, and anti-cheat software may block it. Check the rules for the game or application you use it with.

CustomBind does not modify game files or memory. It is an early, simple project and is currently marked as version `0.3 BETA`.

This project is currently a personal development project.

The license will be added in a future release.

---

## ⭐ About

**CustomBind** is a small project focused on providing simple and accessible key remapping for games and applications.

The goal is to make key remapping easy, lightweight and configurable without requiring changes to the application or game itself.

---

**CustomBind — Simple Key Remapping.**