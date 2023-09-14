#!/usr/bin/python3
"""This module adds a State object from a database."""
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """Adds the State object 'Louisiana' to a given database."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")

    session.add(state)
    session.commit()

    print(f"{state.id}")

    session.close()


if __name__ == "__main__":
    main()
