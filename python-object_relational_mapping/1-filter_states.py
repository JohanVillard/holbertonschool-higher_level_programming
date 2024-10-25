#!/usr/bin/python3
"""This module lists all states starting with N."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connection to the database
    # Create a connexion object
    connection = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,  # This is the default port
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute SQL query
    # Display city starting with a N
    cursor.execute(
        "SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC"
    )

    # Fetch All-at-Once
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and connexion
    cursor.close()
    connection.close()
