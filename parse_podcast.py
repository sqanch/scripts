#!/bin/python3.8

import sys
import os

print(sys.argv)
podcast = sys.argv[1]

link = ""
position = ""
list = podcast.split(" ")

for i in range(len(list)):
    if "Position" in list[i]:
        position = list[i+1]
    elif "Link" in list[i]:
        link = list[i+1]

print("~/.scripts/mpv_parameter \"" + link + " --start=" + position + "\"")
os.system("~/.scripts/mpv_parameter \"" + link + " --start=" + position + "\"")
# os.system("mpv " + link)
