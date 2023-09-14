#!/usr/bin/python3
"""This module lists all State objects from a database."""
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """Lists all State object from a given database."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
