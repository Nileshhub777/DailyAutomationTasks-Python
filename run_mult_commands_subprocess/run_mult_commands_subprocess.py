import subprocess
import os

commands = [
    "echo 'First command.'",
    "echo 'second command'",
    "echo 'Third command.'"
 ]

for command in commands:
    try:
        print(f"Executing: {command}")
        result=subprocess.run(command, shell=True, check=True,text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed.!@! : {e}")