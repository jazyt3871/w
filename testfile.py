import os
import shutil
import subprocess
import sys

def copy_to_startup():
    # Get the current path of the running executable
    current_exe = sys.executable

    # Get the user's Startup folder path
    startup_folder = os.path.join(
        os.getenv("APPDATA"),
        r"Microsoft\Windows\Start Menu\Programs\Startup"
    )

    # Target path where the exe will be copied
    target_path = os.path.join(startup_folder, "MyStartupApp.exe")

    # Only copy if it's not already there
    if current_exe != target_path:
        shutil.copyfile(current_exe, target_path)

if __name__ == "__main__":
    copy_to_startup()
    subprocess.Popen(["notepad.exe"])
