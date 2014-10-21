import csv


class Stock(object):
    __slots__ = ['name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Stock(%r, %r, %r)' % (self.name, self.shares, self.price)

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if not value > 0:
            raise ValueError('Expected a positive integer')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        if not value > 0:
            raise ValueError('Expected a positive float')
        self._price = value

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
