from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQL(Database):
    def connect(self):
        print("MySQL connected")

    def insert(self):
        print("Data inserted into MySQL")

    def close(self):
        print("MySQL connection closed")


class SQLite(Database):
    def connect(self):
        print("SQLite connected")

    def insert(self):
        print("Data inserted into SQLite")

    def close(self):
        print("SQLite connection closed")


mysql = MySQL()
sqlite = SQLite()

mysql.connect()
mysql.insert()
mysql.close()

sqlite.connect()
sqlite.insert()
sqlite.close()