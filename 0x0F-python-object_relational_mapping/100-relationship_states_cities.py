#!/usr/bin/python3
"""This module adds a State object and a City object to a database."""
import sys

from relationship_state import State, Base
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """Adds a State object and a City object to a given database."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    state.cities = [City(name="San Francisco")]

    session.add(state)
    session.commit()

    session.add(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
