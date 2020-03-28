#!/usr/bin/python3
import sys
import MySQLdb
username = str(sys.argv[1])
password = str(sys.argv[2])
db_name = str(sys.argv[3])
conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
query_row = cur.fetchall()
for row in query_row:
    print(row)
cur.close()
conn.close()
