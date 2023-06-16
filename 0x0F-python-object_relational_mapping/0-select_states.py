#!/usr/bin/python3

'''
module: '0-select_states'
    Selects all states from a database
'''

import MySQLdb
import sys

if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_user,
            passwd=mysql_passwd,
            db=db_name
            )

    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close
