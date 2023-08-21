#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    sql_command = """SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities on states.id = cities.state_id ORDER BY cities.id ASC"""
    cursor.execute(sql_command)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
