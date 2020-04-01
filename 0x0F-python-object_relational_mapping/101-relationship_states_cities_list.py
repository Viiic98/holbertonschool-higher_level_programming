#!/usr/bin/python3
""" print all the states with the cities associated """


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

    records = session.query(State).order_by(State.id).all()
    for row in records:
        print("{}: {}".format(row.name, row.id))
        # go through the list of cities that have the relationship
        for city in row.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
