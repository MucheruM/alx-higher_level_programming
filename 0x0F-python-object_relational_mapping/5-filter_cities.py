#!/usr/bin/python3

""" A script that takes in the name of a state as an arg
and list all cities of that state using the database"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, db_name, state_name = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name,
        port=3306,
    )

    cursor = conn.cursor()

    query = """
        SELECT cities.name
        FROM cities
            JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id;
        """
    cursor.execute(query, (state_name,))

    result_set = cursor.fetchall()

    # Concatenate cities.name into a str separated by commas
    cities = ', '.join(row[0] for row in result_set)
    print(cities)

    cursor.close()
    conn.close()
