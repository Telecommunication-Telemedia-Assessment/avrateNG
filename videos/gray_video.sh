#!/bin/bash


ffmpeg -loop 1 -i img.png -y -probesize 8G -c:v ffvhuff -vf scale=-2:1080 -r 60 -pix_fmt yuv444p10le -t 2 "gray.mkv"

# full resolution
#ffmpeg -loop 1 -i img.png -y -probesize 8G -c:v ffvhuff -r 60 -pix_fmt yuv444p10le -t 2 "gray.mkv"
