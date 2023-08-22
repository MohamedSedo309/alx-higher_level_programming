#!/usr/bin/python3
"""
search for a state object by name from
database via python from mysql states table
parameters: username, password, database , state name
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db), pool_pre_ping=True)
    Session = (sessionmaker(bind=engine))
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")
    session.close()
