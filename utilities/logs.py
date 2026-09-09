from datetime import datetime


# Append one activity message to the log file with a short or full timestamp.
def log(message, include_date=False):
    # Startup messages include the date; regular activity only needs the time.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S" if include_date else "%H:%M:%S")
    with open("logs.log", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} {message}\n")
