from .formatter import TableFormatter


class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join([str(x) for x in rowdata]))
