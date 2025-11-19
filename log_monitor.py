import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = datetime.now().strftime("%Y-%m-%d") + ".log"
    filepath = os.path.join(LOG_DIR, filename)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

if __name__ == "__main__":
    log_event("Test log entry")
