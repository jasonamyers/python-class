# descrip.py
#
# Note:  This is only one of many possible implementations.  Experiment.

class BaseDescriptor(object):
    def __init__(self,name):
        self.name = name
    def __get__(self,obj,cls):
        if obj is None:
            return self
        else:
            return obj.__dict__[self.name]
    def __set__(self,obj,value):
        obj.__dict__[self.name] = value
    def __delete__(self,obj):
        raise AttributeError("Can't delete")

# Descriptor that implements type-checking
class Typed(BaseDescriptor):
    expected_type = None
    def __set__(self,obj,value):
        if not isinstance(value,self.expected_type):
            raise TypeError("Expected %s" % self.expected_type)
        super(Typed,self).__set__(obj,value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

# Descriptor that implements domain checking
class DomainChecked(BaseDescriptor):
    def __set__(self,obj,value):
        self.check_domain(value)
        super(DomainChecked,self).__set__(obj,value)

class Positive(DomainChecked):
    def check_domain(self,value):
        if value <= 0:
            raise ValueError("Expected positive")

class Negative(DomainChecked):
    def check_domain(self,value):
        if value >= 0:
            raise ValueError("Expected Negative")

class NonNegative(DomainChecked):
    def check_domain(self,value):
        if value < 0:
            raise ValueError("Expected Nonnegative")

class NonPositive(DomainChecked):
    def check_domain(self,value):
        if value > 0:
            raise ValueError("Expected Nonpositive")

# Mixing it up
class PositiveInteger(Integer,Positive):
    pass

class PositiveFloat(Float,Positive):
    pass

# Sample typed class
class Stock(object):
    name   = String("name")
    shares = PositiveInteger("shares")
    price  = PositiveFloat("price")
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
