import subprocess
import os

commands = [
    "echo 'First command.'",
    "echo 'Second command'",
    "echo 'Third command.'"
    "echo 'Fourth command.'"
 ]

for command in commands:
    try:
        print(f"Executing command: {command}")
        result=subprocess.run(command, shell=True, check=True,text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed.!@! : {e}")