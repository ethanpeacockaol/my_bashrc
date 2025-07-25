import os
import subprocess
# add the todo directory
print('hey add gitsync to Github directory as .gitsync.py right and then add an alias to call it from anywhere')
dirs_to_pull = ["/data/data/com.termux/files/home/x/TODO"]


# deviations... ubuntu does not have an x directory...
# fixes include uhhh changing the tool when you download it to point to the correct todo directory
# or add x directory to ubuntu
# i think i'll just change the path right

# Here is the command that returns a list of strings that represent an ls output


ls_output = subprocess.run("ls", capture_output=True, text=True)
ls_items = ls_output.stdout.split("\n")[:-1]
for item in ls_items:
    print(item)