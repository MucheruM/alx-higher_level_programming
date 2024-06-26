#!/usr/bin/python3

""" Writing a secure code from MySQL injection which takes
an arg and gets the results from an SQL database"""

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
        SELECT * FROM states
        WHERE name LIKE BINARY %s
        ORDER BY states.id;
        """

    cursor.execute(query, (state_name + '%',))

    return_set = cursor.fetchall()

    for row in return_set:
        print(row)

    cursor.close()
    conn.close()
