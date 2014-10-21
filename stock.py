import csv


class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        name, shares, price = row[0].split()
        s = Stock(name, int(shares), float(price))
        portfolio.append(s)
    return portfolio
