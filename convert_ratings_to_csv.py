#!/usr/bin/env python3
"""
    rating convert script

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
import argparse
import json
import sqlite3
import pandas as pd


def lInfo(x):
    print(x)


def lError(x):
    print(x)


def main(params=[]):
    parser = argparse.ArgumentParser(description='avrate++ convert ratings to csv for better handling', epilog="stg7 2017", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dbfilename', type=str, default="ratings.db", help='filename of database with ratings')
    parser.add_argument("--csv_file_prefix", type=str, default="_", help="prefix of csv files")

    a = vars(parser.parse_args())
    lInfo("convert {}".format(a["dbfilename"]))

    connection = sqlite3.connect(a["dbfilename"])

    if not os.path.isfile(a["dbfilename"]):
        lError("your database is not a valid file")
        return

    for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        table = row[0]
        csvtable = a["csv_file_prefix"] + table + ".csv"
        print(f"export table: {table} to {csvtable}")
        df = pd.read_sql_query(f"SELECT * from {table}", connection)
        df.to_csv(csvtable, index=False)

    connection.commit()
    lInfo("done.")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
