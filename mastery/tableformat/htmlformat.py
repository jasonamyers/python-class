from .formatter import TableFormatter


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
