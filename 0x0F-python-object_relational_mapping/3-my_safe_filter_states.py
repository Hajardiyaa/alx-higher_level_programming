#!/usr/bin/python3
"""
Script to display values in the states table where name matches the argument

"""

import MySQLdb
import sys
  """
    Connects to the MySQL server and displays states
    
    Args:
        username (str)
        password (str)
        db_name (str)
        state_name (str)
    """
if __name__ == "__main__":
   
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],  
        passwd=sys.argv[2],  
        db=sys.argv[3],  
        charset="utf8"
    )

    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s;"  
    cur.execute(query, (sys.argv[4],))  
    query_rows = cur.fetchall()  
    for row in query_rows:
        print(row)  
    cur.close() 
    conn.close() 

