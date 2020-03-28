#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = str(sys.argv[1])
    password = str(sys.argv[2])
    db_name = str(sys.argv[3])
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE 'N%'\
                 ORDER BY states.id")
    query_row = cur.fetchall()
    if query_row:
        for row in query_row:
            print(row)
    cur.close()
    conn.close()
