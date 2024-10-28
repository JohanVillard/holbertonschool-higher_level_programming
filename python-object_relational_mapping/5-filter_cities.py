#!/usr/bin/python3
"""This module lists all states in relation with city argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the commands_line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create sql queries
    sql_queries = """
        SELECT DISTINCT sorted_cities.name
        FROM (
                SELECT *
                FROM cities
                ORDER BY cities.id ASC
            ) sorted_cities
        JOIN states
        ON sorted_cities.state_id = states.id
        WHERE states.name = %s
        """

    # Execute protected SQL queries (tuple style)
    cursor.execute(sql_queries, (state_name,))

    # Get and print the results
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    # Clean up
    cursor.close()
    connexion.close()
