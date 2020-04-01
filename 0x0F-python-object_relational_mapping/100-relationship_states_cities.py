#!/usr/bin/python3
""" Add a new state and a city relationed with it """


import sys
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    California = State(name="California")
    California.cities = [City(name="San Francisco")]
    session.add(California)
    session.commit()
    session.close()
