#!/usr/bin/python3
<<<<<<< HEAD
"""
write a script that lists all states
from the database hbtn_0e_0_usa:
Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""
=======
"""write a script that lists all states
from the database hbtn_0e_0_usa"""
>>>>>>> b5871a7581a178ed13c5f621fb4555d6ba20934f
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
<<<<<<< HEAD
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall()]
=======
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
>>>>>>> b5871a7581a178ed13c5f621fb4555d6ba20934f
