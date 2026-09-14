class MySQL:
    def connect(self):
        print("Connected to MySQL database")


class SQLite:
    def connect(self):
        print("Connected to SQLite database")


class Oracle:
    def connect(self):
        print("Connected to Oracle database")


def connect_database(database):
    database.connect()


mysql = MySQL()
sqlite = SQLite()
oracle = Oracle()

connect_database(mysql)
connect_database(sqlite)
connect_database(oracle)