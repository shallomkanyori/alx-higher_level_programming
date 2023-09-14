#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import urllib.parse
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    passwd = urllib.parse.quote_plus(sys.argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], passwd, sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(engine)
