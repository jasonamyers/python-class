# textformat.py
from .formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print("%10s" % h, end=' ')
        print()
        print(("-"*10 + " ")*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print("%10s" % d, end=' ')
        print()
