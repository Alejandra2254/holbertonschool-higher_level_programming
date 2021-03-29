#!/usr/bin/python3
"""Query with SQLAlchemy, creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           encoding='utf-8', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_city = State(name='California', cities=[City(name='San Francisco')])
    session.add(new_city)
    session.commit()
    session.close()
