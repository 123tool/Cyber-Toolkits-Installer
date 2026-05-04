import os
import subprocess

def get_platform():
    if os.path.exists('/data/data/com.termux'):
        return "termux"
    return "linux"

def execute_cmd(command):
    platform = get_platform()
    if platform == "linux" and not command.startswith("sudo"):
        if "apt" in command:
            command = f"sudo {command}"
    
    if platform == "termux":
        command = command.replace("sudo ", "").replace("apt", "pkg")
        
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error saat eksekusi: {e}")
