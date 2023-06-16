#!/usr/bin/python3

'''
module: '3-my_safe_filter_states'
    SQL Injection
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    state_to_search = sys.argv[4]
    cursor = db.cursor()
    q = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(q, (state_to_search,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
