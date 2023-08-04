#!/bin/bash
ffmpeg -framerate 0.5 -pattern_type glob -i '*.png' animation.gif