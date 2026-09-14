from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")


class Oracle(Database):

    def connect(self):
        print("Connected to Oracle")


class PostgreSQL(Database):

    def connect(self):
        print("Connected to PostgreSQL")


databases = [MySQL(), Oracle(), PostgreSQL()]

for database in databases:
    database.connect()