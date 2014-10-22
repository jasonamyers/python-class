from abc import ABC, abstractmethod

class TableFormatter(ABC):

    def leader(self):
        pass

    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError

    def closer(self):
        pass
