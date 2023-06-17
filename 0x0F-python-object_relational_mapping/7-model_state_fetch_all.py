#!/usr/bin/python3

'''
module: '7-model_state_fetch_all'
    Lists all State objects from hbtn_0e_6_usa database
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
