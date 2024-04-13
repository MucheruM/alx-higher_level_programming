#!/usr/bin/python3

""" A Script that assesses information in SQL server"""

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
        SELECT * FROM states
        ORDER BY states.id;
        """
        )

    result_set = cursor.fetchall()

    for row in result_set:
        print(row)

    cursor.close()
    conn.close()
