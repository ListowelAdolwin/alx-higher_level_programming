#!/usr/bin/python3
"""
List all cities using their state names
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))

    states = cur.fetchall()

    print(", ".join([row[0] for row in states]))
    cur.close()
    db.close()
