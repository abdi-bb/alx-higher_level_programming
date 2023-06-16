#!/usr/bin/python3

'''
module: '1-filter_states'
    States starting with N
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[
        2], host='localhost', port=3306, db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
