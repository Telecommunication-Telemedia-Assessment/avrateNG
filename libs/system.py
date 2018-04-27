#!/usr/bin/env python3
"""
    system macros
    see also projects from https://github.com/stg7

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
import subprocess


def shell_call(call):
    """
    Run a program via system call and return stdout + stderr.
    @param call programm with command line parameters, e.g. "ls -1 /"
    @return stdout and stderr of programm call
    """
    try:
        output = subprocess.check_output(call, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
    except Exception as e:
        output = str(e)
    return output


def read_file(file_name):
    """
    read a text file into a string
    :file_name file to open
    :return content as string
    """
    f = open(file_name, "r")
    content = "".join(f.readlines())
    f.close()
    return content


def get_shebang(file_name):
    """
    read shebang of a file
    :file_name file to open
    :return shebang
    """
    try:
        f = open(file_name, "r")
        lines = f.readlines()
        f.close()
        if len(lines) == 0:
            return ""
        shebang = lines[0]
        return shebang
    except Exception as e:
        return ""


def create_dir_if_not_exists(dir):
    try:
        os.stat(dir)
    except:
        os.mkdir(dir)


def get_prog_name():
    """
    @return name of script
    """
    return os.path.basename(sys.argv[0])


if __name__ == "__main__":
    print("\033[91m[ERROR]\033[0m lib is not a standalone module")
    exit(-1)
