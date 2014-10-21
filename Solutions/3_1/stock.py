# stock.py

class Stock(object):
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

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
