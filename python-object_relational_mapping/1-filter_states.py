#!/usr/bin/python3
"""This module lists all states starting with N from hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connection to the database
    # Create a connexion object
    connexion = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,  # This is the default port
    )

    # Create a cursor object
    cursor = connexion.cursor()

    # Search city starting with a N
    cursor.execute(
        """
        SELECT *
        FROM states
        WHERE name
        LIKE BINARY 'N%'
        ORDER BY id ASC
        """
    )

    # Fetch All-at-Once
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and connexion
    cursor.close()
    connexion.close()
