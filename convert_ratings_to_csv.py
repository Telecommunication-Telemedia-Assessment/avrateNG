#!/usr/bin/env python3
import os
import sys
import argparse
import json
import sqlite3

# load libs from lib directory
import loader
from log import *
from system import *


def main(params=[]):
    parser = argparse.ArgumentParser(description='avrate++ convert ratings to csv for better handling', epilog="stg7 2017", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dbfilename', type=str, default="ratings.db", help='filename of database with ratings')
    parser.add_argument('--cvsfilename', type=str, default="ratings.csv", help='filename of cvs file for exporting')

    argsdict = vars(parser.parse_args())
    lInfo("convert {} to {}".format(argsdict["dbfilename"], argsdict["cvsfilename"]))

    connection = sqlite3.connect(argsdict["dbfilename"])

    if not os.path.isfile(argsdict["dbfilename"]):
        lError("your database is not a valid file")
        return

    schema = {}
    for row in connection.execute("""pragma table_info('ratings') """):
        schema[row[1]] = ""
    schema = sorted(schema.keys())

    with open(argsdict["cvsfilename"], "w") as csv:
        csv.write(",".join(schema) + "\n")
        for row in connection.execute("""select {} from ratings; """.format(",".join(schema))):
            csv_values = [str(row[i]) for i in range(len(row))]
            csv.write(",".join(csv_values) + "\n")

    connection.commit()
    lInfo("done.")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
