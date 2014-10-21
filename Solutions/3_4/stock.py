# stock.py

class Stock(object):
    __slots__ = ('name','_shares','_price')
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('shares must be non-negative')
        self._shares = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if not isinstance(value,float):
            raise TypeError('Expected a float')
        if value < 0:
            raise ValueError('price must be non-negative')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self,nshares):
        self.shares -= nshares

# A function that reads a file into a list of Stocks
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split()
        record = Stock(fields[0],int(fields[1]),float(fields[2]))
        portfolio.append(record)
    return portfolio

