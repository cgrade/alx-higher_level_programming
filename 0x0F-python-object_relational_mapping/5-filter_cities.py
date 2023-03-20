#!/usr/bin/python3
"""
A script that takes in the name of
a state and an argument and lists
all `cities` of that state from the
database `hbtn_0e_4_usa`
"""
if __name__ == "__main__":
    """import required module"""
    import MySQLdb as db
    from sys import argv

    db_connector = db.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    db_cursor = db_connector.cursor()
    db_cursor.execute("""SELECT cities.id, cities.name FROM cities
            JOIN states on cities.state_id = states.id
            WHERE states.name LIKE BINARY %(state_name)s
            ORDER BY cities.id""", {'state_name': argv[4]})
    row_fetched = db_cursor.fetchall()
    print(', '.join([row[1] for row in row_fetched]))
