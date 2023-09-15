#!/usr/bin/python3
"""Lists all states filtered by name from a database."""
import MySQLdb
import sys


def main():
    """Lists all states filtered by a given name from a given database."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()

    query = """SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id ASC""".format(state_name)

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
