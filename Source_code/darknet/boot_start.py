#!/usr/bin/python
import os
command = "cd /home/new/Desktop/opencv/opencv-3.4.0/build/darknet; python3 detect_start.py"
os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")

