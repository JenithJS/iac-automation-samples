import os
import time

folder = "./logs"
expiry_seconds = 24 * 60 * 60

if not os.path.exists(folder):
    print("Logs folder not found.")
    exit()

now = time.time()

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isfile(path):
        if now - os.stat(path).st_mtime > expiry_seconds:
            os.remove(path)
            print(f"Deleted old file: {file}")
