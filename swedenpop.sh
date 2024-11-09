#!/bin/bash

DAY=$1
MONTH=$2
URL="http://bermudafunk.org/fileadmin/mp3_uploads/2024-$MONTH-${DAY}_10.mp3"
mpv $URL
