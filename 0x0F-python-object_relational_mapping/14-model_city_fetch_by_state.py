#!/usr/bin/python3
'''
module: '14-model_city_fetch_by_state'
    Script that prints all City objects from a database
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).scalar()
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
