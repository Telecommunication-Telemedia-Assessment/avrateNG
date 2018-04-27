#!/usr/bin/env python3
"""
    loader script

    This file is part of avrateNG.
    avrateNG is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    avrateNG is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with avrateNG.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys

for m in filter(lambda x: ".zip" in x, os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/libs")):
    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/libs/" + m)

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/libs/")
