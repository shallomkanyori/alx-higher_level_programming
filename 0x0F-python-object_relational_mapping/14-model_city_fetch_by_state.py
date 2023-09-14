#!/usr/bin/python3
"""This module prints all City objects with their state name from a database.
"""
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """Prints all City objects with their state names from a given database."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(City.id, City.name, State.name)
                    .join(State, City.state_id == State.id)
                    .order_by(City.id))

    for row in query.all():
        city_id = row[0]
        city_name = row[1]
        state_name = row[2]
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()


if __name__ == "__main__":
    main()
