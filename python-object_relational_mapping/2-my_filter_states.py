#!/usr/bin/python3
"""This module displays values."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion with database
    connexion = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,
    )

    # Create a cursor
    cursor = connexion.cursor()

    # Execute a SQL query
    sql = "SELECT * \
            FROM states \
            WHERE name = '{}' \
            ORDER BY states.id ASC".format(state_name_searched)
    cursor.execute(sql)

    # All fetched at once
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    connexion.close()
