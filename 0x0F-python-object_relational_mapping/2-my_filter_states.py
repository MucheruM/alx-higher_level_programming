#!/usr/bin/python3

""" A script that takes in an argument and displays all values
in the states table of the database where name matches the arg"""

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

    # This query is unsafe for SQL injection
    query = """
            SELECT * FROM states
            WHERE name LIKE BINARY 'Arizona%'
            ORDER BY states.id
        """.format(state_name)

    cursor.execute(query)

    return_set = cursor.fetchall()

    for row in return_set:
        print(row)

    cursor.close()
    conn.close()
