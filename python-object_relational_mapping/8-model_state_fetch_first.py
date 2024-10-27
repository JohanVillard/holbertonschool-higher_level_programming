#!/usr/bin/python3
"""This module prints the first `State` object from `hbtn_0e_6_usa`."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get the commands-line:
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connection
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get first object
    state = session.query(State).order_by(State.id.asc()).first()
    if not state:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    session.close()
