#!/usr/bin/python3
"""Start link class to table in database
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), encoding='utf-8',
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for delete_this in session.query(State).filter(State.name.like('%a%')):
        session.delete(delete_this)
    session.commit()
    session.close()
