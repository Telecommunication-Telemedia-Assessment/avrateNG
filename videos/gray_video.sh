#!/bin/bash

ffmpeg -loop 1 -i img.png -y -probesize 8G -c:v ffvhuff -r 60 -pix_fmt yuv444p10le -t 2 "gray.mkv"
