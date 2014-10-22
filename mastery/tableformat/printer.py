from .formatter import TableFormatter
def print_table(objects, attributes, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.leader()
    formatter.headings(attributes)
    for obj in objects:
        rowdata = [getattr(obj, attr, 'undef') for attr in attributes]
        formatter.row(rowdata)
    formatter.closer()
