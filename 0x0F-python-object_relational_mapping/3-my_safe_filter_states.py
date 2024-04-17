#!/usr/bin/python3

""" Writing a secure code from MySQL injection which takes and ar gets results from an SQL database"""

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

    cursor.execute(
        """
        SELECT * FROM states
        WHERE name LIKE BINARY %s
        ORDER BY states.id;
        """,
        (state_name,),
    )

    return_set = cursor.fetchall()

    for row in return_set:
        print(row)

    cursor.close()
    conn.close()
