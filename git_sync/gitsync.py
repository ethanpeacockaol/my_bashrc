import os

# add the todo directory
# deviations... ubuntu does not have an x directory...
# fixes include uhhh changing the tool when you download it to point to the correct todo directory
# or add x directory to ubuntu
# i think i'll just change the path right

# Here is the command that returns a list of strings that represent an ls output
import subprocess

ls_output = subprocess.run("ls", capture_output=True, text=True)
ls_items = ls_output.stdout.split("\n")[:-1]
for item in ls_items:
    print(item)