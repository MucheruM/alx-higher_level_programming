#!/usr/bin/python3

""" Write a script that lists all cities from the database """

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, db_name = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name,
        port=3306,
    )

    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT cities.id, cities.name, state.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
        """
    )

    result_set = cursor.fetchall()

    for row in result_set:
        print(row)

        cursor.close()
        conn.close()
