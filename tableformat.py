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


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for h in headers:
            print('%10s' % h, end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print('%10s' % d, end=' ')
        print()


class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join([str(x) for x in rowdata]))


class HTMLTableFormatter(TableFormatter):

    def leader(self):
        print('<table>')

    def closer(self):
        print('</table>')

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<td>%s</td>' % h, end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>%s</td>' % d, end='')
        print('</tr>')


def print_table(objects, attributes, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.leader()
    formatter.headings(attributes)
    for obj in objects:
        rowdata = [getattr(obj, attr, 'undef') for attr in attributes]
        formatter.row(rowdata)
    formatter.closer()

def old_print_table(objects,attributes):
    lengths = {}
    fmts = {}
    header = ''
    for attr in attributes:
        attrlen = len(str(attr))

        lengths[attr] = max([max([len(str(getattr(thing, attr, 'undef'))) for thing in objects]), len(str(attr))]) + 2
        print('{:>{width}}'.format(attr, width=lengths[attr]), end=' ')
    print()
    for attr in attributes:
        print('-' * lengths[attr] + ' ', end=' ')
    print()
    for obj in objects:
        for attr in attributes:
            print('{:>{width}}'.format(getattr(obj, attr, 'undef'), width=lengths[attr]), end=' ')
        print()
