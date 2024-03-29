#!/usr/bin/python3
"""
List all cities from the database specified
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
                "SELECT cities.id, cities.name, states.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id ASC;"
        )

    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
