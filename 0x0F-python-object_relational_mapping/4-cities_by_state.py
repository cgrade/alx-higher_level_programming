#!/usr/bin/python3
"""
A script that lists all rows form the
citiees table of `hbtn_0e_4_usa` database
"""

"""check if module is running on `main`"""

if __name__ == '__main__':
    """import necesary dependencies"""

    import MySQLdb as db
    from sys import argv

    db_connector = db.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    db_cursor = db_connector.cursor()
    db_cursor.execute("""SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC""")
    row_fetched = db_cursor.fetchall()
    for row in row_fetched:
        print(row)
