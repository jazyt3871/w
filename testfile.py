import os
import shutil
import sys
import subprocess

def add_to_startup():
    # Get path to current exe
    current_exe = sys.executable
    # Get startup folder path
    startup_folder = os.path.join(os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup")
    target_path = os.path.join(startup_folder, "MyApp.exe")

    if current_exe != target_path:
        try:
            shutil.copyfile(current_exe, target_path)
            subprocess.Popen([target_path])
            sys.exit()
        except Exception as e:
            print(f"Failed to add to startup: {e}")

def main():
    # Your code here – in this example, open Notepad
    subprocess.Popen(["notepad.exe"])

if __name__ == "__main__":
    add_to_startup()
    main()
