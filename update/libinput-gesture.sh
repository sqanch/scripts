#!/bin/bash

cd /home/max/software/libinput-gestures
git pull
sudo ./libinput-gestures-setup install
libinput-gestures-setup restart
