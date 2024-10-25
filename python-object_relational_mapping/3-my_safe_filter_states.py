#!/usr/bin/python3
"""This module explains SQL injection."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the commands-line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_search = sys.argv[4]

    # Connect to database
    connexion = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,
    )

    # Create a cursor
    cursor = connexion.cursor()

    # Execute safe SQL query
    sql = "SELECT * FROM states WHERE states.name = %s ORDER BY states.id ASC"
    # Place state_name_search in an immutable tuple
    cursor.execute(sql, (state_name_search,))

    # Get the results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    connexion.close()
