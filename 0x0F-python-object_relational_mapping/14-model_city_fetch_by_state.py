#!/usr/bin/python3
"""
return all cities from database MySQl 
via python code
parameters: username, password, database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)
    for q in query:
        print("{:s}: ({:d}) {:s}".format(q[0], q[1], q[2]))

    session.close()
