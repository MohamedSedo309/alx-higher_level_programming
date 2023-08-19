#!/usr/bin/python3
"""
write a script that lists all states
from the database hbtn_0e_0_usa:
Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
