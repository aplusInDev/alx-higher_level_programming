#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
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
    SELECT * FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY id
    """
    cursor.execute(sql_select)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
