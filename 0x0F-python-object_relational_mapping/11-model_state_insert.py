#!/usr/bin/python3
'''
module: '11-model_state_insert'
    Script that adds State object "Louisiana" to a database
'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="Louisiana"))
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print(f'{state.id}')

    session.close()
