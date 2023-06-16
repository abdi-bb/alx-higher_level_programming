#!/usr/bin/python3

'''
module: ' 1-filter_states'
    Selects all states beginning with N from a database
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[
        2], host='localhost', port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
