#!/usr/bin/python3
import sys
import MySQLdb
username = str(sys.argv[1])
password = str(sys.argv[2])
db_name = str(sys.argv[3])
name = str(sys.argv[4])
conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT c.name\
            FROM cities AS\
            INNER JOIN states AS s\
            ON c.state_id = s.id\
            WHERE s.name = %s", (name,))
rows = cur.fetchall()
for i in range(cur.rowcount - 1):
    print("%s, " % rows[i], end="")
print("%s" % rows[i + 1])
cur.close()
conn.close()
