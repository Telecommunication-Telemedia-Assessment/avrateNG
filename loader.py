#!/usr/bin/env python3
"""
    Loader

    import modules from zip files that are stored in ./libs/ directory

    author: Steve Göring
    contact: stg7@gmx.de
    2014
"""

import os
import sys

for m in filter(lambda x: ".zip" in x, os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/libs")):
    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/libs/" + m)

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/libs/")
