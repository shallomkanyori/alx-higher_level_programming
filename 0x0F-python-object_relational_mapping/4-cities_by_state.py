#!/usr/bin/python3
"""Lists all cities with their states from a database."""
import MySQLdb
import sys


def main():
    """Lists all cities with their states from a given database."""

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                     FROM cities
                          LEFT JOIN states
                          ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
