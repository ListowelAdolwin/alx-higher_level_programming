#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

#    engine = create_engine(
 #       f"mysql+pymysql://{sys.argv[1]}:{sys.argv[2]}\
  #      @localhost/{sys.argv[3]}?host=localhost?port=3306")
   
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()

    for name, id in Session.query(State.name, State.id):
        print("{}: {}".format(id, name))

