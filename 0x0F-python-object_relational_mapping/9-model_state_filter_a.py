#!/usr/bin/python3
"""
    A Script that uses SQLalchemy to map
    Python class to database table, and Lists
    all hte state objects from the database passed

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1],
                argv[2],
                argv[3],
                pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            print("{}: {}".format(state.id, state.name))
