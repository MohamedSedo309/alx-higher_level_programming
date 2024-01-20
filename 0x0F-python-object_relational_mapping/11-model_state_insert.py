#!/usr/bin/python3
"""
insert a new record
database via python from mysql states table
parameters: username, password, database
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
    lous = State(name="Louisiana")
    session.add(lous)
    session.commit()

    print("{:d}".format(lous.id))

    session.close()
