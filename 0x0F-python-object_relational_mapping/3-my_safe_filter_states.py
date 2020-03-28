#!/usr/bin/python3
""" script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections! """

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = str(sys.argv[1])
    password = str(sys.argv[2])
    db_name = str(sys.argv[3])
    name = str(sys.argv[4])
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s", (name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
