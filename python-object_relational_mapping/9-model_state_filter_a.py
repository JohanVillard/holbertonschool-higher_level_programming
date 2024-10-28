#!/usr/bin/python3
"""This module lists all `State` containing `a` from `hbtn_0e_6_usa`."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get the commands-line:
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create connection
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create tables
    Base.metadata.create_all(engine)

    # Create and instance a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get State containing a
    query = (
        session.query(State)
        .filter(State.name.ilike("%a%"))
        .order_by(State.id.asc())
        .all()
    )

    # Print result
    for state in query:
        print(f"{state.id}: {state.name}")

    session.close()
