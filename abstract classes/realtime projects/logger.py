from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self):
        pass


class FileLogger(Logger):

    def log(self):
        print("Logging to file")


class DatabaseLogger(Logger):

    def log(self):
        print("Logging to database")


class ConsoleLogger(Logger):

    def log(self):
        print("Logging to console")


FileLogger().log()
DatabaseLogger().log()
ConsoleLogger().log()