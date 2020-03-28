#!/usr/bin/python3
import sys
import MySQLdb
username = str(sys.argv[1])
password = str(sys.argv[2])
db_name = str(sys.argv[3])
conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT c.id, c.name, states.name\
           FROM cities AS c\
           INNER JOIN states\
           ON c.state_id = states.id\
           ORDER BY c.id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
