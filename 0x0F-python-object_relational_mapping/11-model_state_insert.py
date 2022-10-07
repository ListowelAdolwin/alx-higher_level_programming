#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from sqlalchemy import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()

    newState = State(name='Louisiana')
    Session.add(newState)
    newState = Session.query(State).filter(State.name == 'Louisiana').first()
    Session.commit
    print("{}".format(newState.id))
    Session.close()
