#!/usr/bin/python3
"""
get state objects from database via python from
mysql states table
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

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db))
    Session = (sessionmaker(bind=engine))
    session = Session()
    for i in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(i.id, i.name))
    session.close()
