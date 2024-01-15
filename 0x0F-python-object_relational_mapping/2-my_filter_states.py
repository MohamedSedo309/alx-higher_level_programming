#!/usr/bin/python3
"""
Write a script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        b=argv[3])
    cursor = db.cursor()
    cursor.execute(
        """SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC""".format(argv[4]))
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
