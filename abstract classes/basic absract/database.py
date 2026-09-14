from abc import ABC, abstractmethod
class database(ABC):
    @abstractmethod
    def connect(self):
        pass
class mysqldatabase(database):
    def connect(self):
        print("Connecting to MySQL database...") 
class postgresqldatabase(database):
    def connect(self):
        print("Connecting to PostgreSQL database...") 
mysqldatabase().connect()
postgresqldatabase().connect()        
