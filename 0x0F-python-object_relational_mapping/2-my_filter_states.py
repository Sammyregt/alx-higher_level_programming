#!/usr/bin/python3
"""
    Displays all values in the states table of hbtn_0e_0_usa
    whose name matches argument passed
    ./2-filter_states.py <mysql username> \
                         <mysql password> \
                         <mysql database name> \
                         <mysql states name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306, host="localhost")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
                id ASC".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)

    cur.close()
    db.close()
