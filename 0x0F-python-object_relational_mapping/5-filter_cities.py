#!/usr/bin/python3
"""Lists all cities of a state from a database."""
import MySQLdb
import sys


def main():
    """Lists all cities of a given state (safely) from a given database."""

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()

    cur.execute("""SELECT cities.name
                     FROM cities
                    WHERE state_id =
                          (SELECT id
                             FROM states
                            WHERE name = %s)
                    ORDER BY cities.id ASC""", (state_name, ))

    rows = cur.fetchall()

    cities = (row[0] for row in rows)
    print(*cities, sep=", ")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
