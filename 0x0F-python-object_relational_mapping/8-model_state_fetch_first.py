#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()

    results = Session.query(State.name, State.id).order_by(State.id).first()
    if results:
        print("{}: {}".format(results.id, results.name))

    else:
        print("Nothing")
