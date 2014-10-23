import csv
class Descriptor(object):
    def __init__(self, name):
        self.name = name
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class Typed(Descriptor):
    expected_type = None
    def __init__(self,name):
        self.name = name
    def __get__(self,obj,cls):
        if obj is None:
            return self
        else:
            return obj.__dict__[self.name]
    def __set__(self,obj,value):
        if not isinstance(value,self.expected_type):
            raise TypeError("Expected %s" % self.expected_type)
        super(Typed, self).__set__(obj, value)
    def __delete__(self,obj):
        raise AttributeError("Can't delete")

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = (float, int)

class String(Typed):
    expected_type = str

class Positive(Descriptor):
    def __set__(self, obj, value):
        if not value > 0:
            raise ValueError("Expected positive integer")
        super(Positive, self).__set__(obj, value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

def typecheck(**kwargs):
    def decorate(cls):
        for field, val_type in kwargs.items():
            setattr(cls, field, val_type(field))
        return cls
    return decorate

class Stock(object):
    name = String("name")
    shares = PositiveInteger("shares")
    price = PositiveFloat("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Stock(%r, %r, %r)' % (self.name, self.shares, self.price)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


class SimpleStock(object):

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price


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


def print_portfolio(portfolio):
    formatter = TextTableFormatter()
    print_table(portfolio, ['name','shares','price'], formatter)


