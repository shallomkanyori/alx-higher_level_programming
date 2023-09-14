#!/usr/bin/python3
"""This module prints all State objects with their City object from a database.
"""
import sys

from relationship_state import State, Base
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, selectinload


def main():
    """Prints all State objects with their City objects from a given database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(State)
                    .options(selectinload(State.cities))
                    .order_by(State.id))

    for state in query.all():
        print(f"{state.id}: {state.name}")

        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    main()
