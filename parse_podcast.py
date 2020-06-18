#!/bin/python3.8

import sys
import os

podcast = sys.argv[1]

link = ""
position = ""
list = podcast.split(" ")

for i in range(len(list)):
    if "Position" in list[i]:
        position = list[i+1].replace("\n", "")
    elif "Link" in list[i]:
        link = list[i+1].replace("\n", "")
    elif "http" in list[i]:
        link = list[i]

command = "~/.scripts/mpv_parameter \"" + link + " --load-unsafe-playlists\""
execute = command
if position != "":
    execute = command[:-1] + " --start=" + position + "\""

if len(sys.argv) > 2:
    time = sys.argv[2]
    execute = command[:-1] + " --start=" + time + "\""

print(execute)
os.system(execute)
# os.system("mpv " + link)
