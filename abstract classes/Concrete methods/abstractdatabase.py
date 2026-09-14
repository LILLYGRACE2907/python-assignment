from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        print("Database: MySQL")


class MySQL(Database):

    def connect(self):
        print("Connected to database")


d = MySQL()
d.connect()
d.display_database_name()