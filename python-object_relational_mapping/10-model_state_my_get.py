#!/usr/bin/python3
"""This module lists all `State` objects from `hbtn_0e_6_usa`."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City
if __name__ == "__main__":
    # Get the commands-line:
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    # Create connection
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create tables
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)

    # Instance a session
    session = Session()

    query = (
        session.query(State)
        .filter(State.name == state_name_to_search)
        .all()
    )
    if not query:
        print("Not found")
    else:
        for state in query:
            print(state.id)

    session.close()
