# descrip.py

class Descriptor(object):
    def __init__(self,name):
        self.name = name
    def __get__(self,obj,cls):
        print("%s:__get__ %s %s" % (self.name, obj, cls))
    def __set__(self,obj,value):
        print("%s:__set__ %s %s" % (self.name, obj, value))
    def __delete__(self,obj):
        print("%s:__delete__ %s" % (self.name, obj))

class Typed(object):
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
        obj.__dict__[self.name] = value
    def __delete__(self,obj):
        raise AttributeError("Can't delete")

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

# Sample typed class
class Stock(object):
    name   = String("name")
    shares = Integer("shares")
    price  = Float("price")
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
