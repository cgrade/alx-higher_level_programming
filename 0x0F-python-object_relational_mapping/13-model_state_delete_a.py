#!/usr/bin/python3
""" A script that changes/updates the name
    of a `State` object from the database
    `hbtn_0e_6_usa`
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1],
                argv[2],
                argv[3],
                pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = session.query(State).filter(State.name.contains('a'))
    if new_state is not None:
        for state in new_state:
            session.delete(state)
    session.commit()
    session.close()
