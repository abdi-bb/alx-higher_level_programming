#!/usr/bin/python3

'''
module: '2-my_filter_states'
    Displays all values where name matches the passed argument
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[
        2], host='localhost', port=3306, db=sys.argv[3])
    state = sys.argv[4]
    cursor = db.cursor()
    q = 'SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY id'
    cursor.execute(q.format(state))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
