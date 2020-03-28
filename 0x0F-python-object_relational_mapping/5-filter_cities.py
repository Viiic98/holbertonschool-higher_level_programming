#!/usr/bin/python3
""" script that takes in the name of a state as an argument
    and lists all cities of that state, using the
    database hbtn_0e_4_usa """

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
    cur.execute("SELECT c.name\
                 FROM cities AS c\
                 INNER JOIN states AS s\
                 ON c.state_id = s.id\
                 WHERE s.name = %s", (name,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
