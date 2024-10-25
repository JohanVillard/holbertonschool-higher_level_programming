#!/usr/bin/python3
"""This module lists cities from hbtn_0e_4_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the commands-line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connexion
    connexion = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,
    )

    # Create a cursor
    cursor = connexion.cursor()

    # Execute SQL queries
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states \
        ON cities.state_id = states.id \
        ORDER BY cities.id"
    )

    # Get the results
    rows = cursor.fetchall()

    # print the results
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    connexion.close()
