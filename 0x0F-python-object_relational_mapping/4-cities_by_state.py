#!/usr/bin/python3

'''
module: '4-cities_by_state'
    Script that lists all cities from a database
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    q = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.states_id = state.id
    ORDER BY cities.id
    """
    cur.execute(q)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
