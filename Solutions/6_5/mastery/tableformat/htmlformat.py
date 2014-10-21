# htmlformat.py
from .formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    def start(self):
        print('<table>')

    def headings(self, headers):
        print("<tr>", end=' ')
        for h in headers:
            print("<th>%s</th>" % h, end=' ')
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end=' ')
        for d in rowdata:
            print("<td>%s</td>" % d, end=' ')
        print("</tr>")

    def end(self):
        print('</table>')
