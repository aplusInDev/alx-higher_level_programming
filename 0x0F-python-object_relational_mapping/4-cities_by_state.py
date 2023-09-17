#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = db.cursor()
    sql_select = """
    SELECT cities.id, cities.name, states.name FROM cities JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id
    """
    cursor.execute(sql_select)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
