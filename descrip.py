class Descriptor(object):

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        print('%s:__delete__' % self.name)


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

def typecheck(**kwargs):
        def decorate(cls):
            for field, val_type in kwargs.items():
                setattr(cls, field, val_type(field))
            return cls
        return decorate

class typedmeta(type):
    def __new__(cls, class_name, bases, methods):
        for key, value in methods.items():
            if isinstance(value, type) and issubclass(value, Typed):
                methods[key] = value(key)
        return type.__new__(cls, class_name, bases, methods)


class typedobject(metaclass=typedmeta):
    pass
