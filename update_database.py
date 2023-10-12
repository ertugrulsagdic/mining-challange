import subprocess
import os

# Configuration
DEVGPT_REPO_URL = 'https://github.com/NAIST-SE/DevGPT.git'
CLONE_DIR = 'DevGPT'  # The directory where you want to clone or pull DevGPT

def run_command(command):
    """Utility function to run shell commands."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    
    if process.returncode != 0:
        print(f"Error executing command: {command}\n{error.decode()}")
    return output.decode()

"""Clone or update the DevGPT repository."""
if os.path.exists(CLONE_DIR):
    # If the directory exists, navigate and pull the latest changes
    os.chdir(CLONE_DIR)
    run_command('git pull origin main')
else:
    # Otherwise, clone the repository
    run_command(f'git clone {DEVGPT_REPO_URL} {CLONE_DIR}')
