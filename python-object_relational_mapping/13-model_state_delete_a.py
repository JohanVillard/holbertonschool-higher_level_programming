#!/usr/bin/python3
"""This module changes the name of a `State` from a `hbtn_0e_6_usa`."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
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

    # Create tables
    Base.metadata.create_all(engine)

    # Create a new session and a new instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the delete query
    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False
    )

    # Validate changes in db
    session.commit()

    session.close()
