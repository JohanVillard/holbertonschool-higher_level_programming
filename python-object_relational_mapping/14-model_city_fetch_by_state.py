#!/usr/bin/python3
"""This module prints all `City` from `hbtn_0e_14_usa`."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get the commands-line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connexion
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create table
    Base.metadata.create_all(engine)

    # Create and instance a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Build a query
    cities_states = session.query(City, State).join(State).order_by(City.id.asc()).all()
    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
