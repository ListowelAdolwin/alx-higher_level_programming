#!/usr/bin/python3


if __name__ == '__main__':
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], port=3307, db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
