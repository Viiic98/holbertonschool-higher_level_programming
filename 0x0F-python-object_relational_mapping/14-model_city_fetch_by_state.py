#!/usr/bin/python3
""" Script that list all cities doing a join using sqlalchemy """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    fil = City.state_id == State.id
    for row in session.query(City, State).filter(fil).all():
        print('{}: ({}) {}'.format(row.State.name, row.City.id, row.City.name))

    session.close()
