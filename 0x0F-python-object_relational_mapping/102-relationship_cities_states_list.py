#!/usr/bin/python3
"""This module lists all City objects from a database."""
import sys

from relationship_state import State, Base
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, joinedload


def main():
    """Lists all City object from a given database."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(City)
                    .options(joinedload(City.state))
                    .order_by(City.id))

    for city in query.all():
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()


if __name__ == "__main__":
    main()
