# formatter.py
from abc import ABC, abstractmethod

class TableFormatter(ABC):
    def start(self):
        pass

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

    def end(self):
        pass
