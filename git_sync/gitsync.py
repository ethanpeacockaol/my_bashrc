import os
import subprocess
# hey comment me out when you install the gitsync command into aliases (.bashrc) and place gitsync.py in the github dir named .gitsync
print('hey add gitsync to Github directory as .gitsync.py right and then add an alias to call it from anywhere')
dirs_to_pull = ["/data/data/com.termux/files/home/x/TODO"]
prepend = "/data/data/com.termux/files/home/x/Github/"
status = ["TODO"]

ls_output = subprocess.run("ls", capture_output=True, text=True)
ls_items = ls_output.stdout.split("\n")[:-1]
status += ls_items

for item in ls_items:
    dirs_to_pull += [f"{prepend}{item}"]

print("________________Git Sync_______________________")
i = 0
for dirx in dirs_to_pull:
    print(f"DIRECTORY: {status[i]}")
    os.system(f"cd {dirx} && git pull")
    print("\n\n")
    i += 1

print("\n\nGit Sync Done.")
print("_______________________________________________")