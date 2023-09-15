#!/usr/bin/python3
"""This module prints all State objects with their City object from a database.
"""
import sys

from relationship_state import State, Base
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, joinedload


def main():
    """Prints all State objects with their City objects from a given database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State)
                     .options(joinedload(State.cities))
                     .order_by(State.id)
                     .all())

    for state in states:
        print(f"{state.id}: {state.name}")

        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    main()
