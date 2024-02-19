#!/usr/bin/python3
"""
 display the values in"states table" of hbtn_0e_0_usa  when it s a match
"""

import MySQLdb
import sys

def filter_states(username: str, password: str, db_name: str, state_name: str):
    """
    Connects to the MySQL server and filters states based on the provided state name.
    
    Args:
        username (str)
        password (str)
        db_name (str)
        state_name (str)
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password db_name state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:]

    filter_states(username, password, db_name, state_name)

