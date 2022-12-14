#!/usr/bin/python3
"""
    Lists all states with a name starting with N
    from the database hbtn_0e_0_usa.
    usage: ./1-filter_states.py <mysql username> \
                                <mysql password> \
                                <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    states = cur.fetchall()
    [print(state) for state in states if state[1][0] == "N"]
