from datetime import datetime


def log(message, include_date=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S" if include_date else "%H:%M:%S")
    with open("logs.log", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} {message}\n")
