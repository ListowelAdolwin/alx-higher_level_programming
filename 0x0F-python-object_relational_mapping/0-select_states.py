#!/usr/bin/python3
"""
List all states from the database specified
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
