import subprocess
import os

commands = [
    "echo '1st command.'",
    "echo '2nd command'",
    "echo 'Third command.'"
    "echo 'fourth command.'"
 ]

for command in commands:
    try:
        print(f"Executing command: {command}")
        result=subprocess.run(command, shell=True, check=True,text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed.!@! : {e}")