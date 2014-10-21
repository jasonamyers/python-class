# printer.py
from .formatter import TableFormatter

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')

    formatter.start()
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname, 'undef') for fieldname in fields]
        formatter.row(rowdata)
    formatter.end()
