#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
raspistill -o /home/pi/photo_scripts/image.jpg

python /home/pi/photo_scripts/photo_send.py

rm -rf /home/pi/photo_scripts/image.jpg
