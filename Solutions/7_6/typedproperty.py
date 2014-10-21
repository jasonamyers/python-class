# typedproperty.py
#
# A utility function that makes typed properties on a class

def typed_property(name, expected_type):
    # Private attribute name where value is actually stored
    private_name = "_" + name
    
    # Getter
    def getter(self):
        return getattr(self,private_name)

    # Setter
    def setter(self,value):
        if not isinstance(value, expected_type):
            raise TypeError("Expected %s" % expected_type)
        setattr(self,private_name,value)
    
    return property(getter,setter)

from functools import partial

String = partial(typed_property,  expected_type=str)
Integer = partial(typed_property,  expected_type=int)
Float = partial(typed_property,  expected_type=float)

if __name__ == '__main__':
    class Stock(object):
        name = typed_property("name",str)
        shares = typed_property("shares", int)
        price = typed_property("price", float)

        def __init__(self,name,shares,price):
            self.name = name
            self.shares = shares
            self.price = price
        
    class Stock2(object):
        name = String("name")
        shares = Integer("shares")
        price = Float("price")

        def __init__(self,name,shares,price):
            self.name = name
            self.shares = shares
            self.price = price
        


    

    
    
