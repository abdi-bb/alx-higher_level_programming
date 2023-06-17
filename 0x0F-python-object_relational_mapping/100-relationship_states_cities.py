#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.add(city)
    session.commit()

    session.close()
