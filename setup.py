import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIREMENTS_FILE = ROOT / "requirements.txt"
APP_FILE = ROOT / "main.py"


def clear_console():
    """Clear the terminal for a cleaner setup and launch experience."""
    os.system("cls" if os.name == "nt" else "clear")


def install_requirements():
    """Install all required dependencies for the active Python environment."""
    if not REQUIREMENTS_FILE.exists():
        raise FileNotFoundError(f"Missing requirements file: {REQUIREMENTS_FILE}")

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)],
        cwd=str(ROOT),
    )


def launch_app():
    """Start the CustomBind application using the same Python interpreter."""
    if not APP_FILE.exists():
        raise FileNotFoundError(f"Missing app entrypoint: {APP_FILE}")

    subprocess.call([sys.executable, str(APP_FILE)], cwd=str(ROOT))


def main():
    print("CustomBind setup")
    print("This will install the required dependencies and start the app.")
    choice = input("Continue? [Y/N]: ").strip().lower()

    if choice in {"y", "yes"}:
        install_requirements()
        clear_console()
        launch_app()
    else:
        print("Setup cancelled. Run 'python main.py' after installing requirements manually.")


if __name__ == "__main__":
    main()