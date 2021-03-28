#!/usr/bin/python3
"""Start link class to table in database
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)
    session = Session()
    for results in session.query(State).order_by(State.id):
        print("{}: {}".format(results.id, results.name))
    session.close()
