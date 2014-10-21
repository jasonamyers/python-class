# sample.py

from logcall import logged, loglevel, logmethods, loggetattribute
import logging

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y


@loglevel(logging.CRITICAL)
def a():
    pass

@loglevel(logging.DEBUG)
def b():
    pass

@logmethods
class A(object):
    def __init__(self):
        pass
    def x(self):
        pass
    def y(self):
        pass

@loggetattribute
class B(object):
    def __init__(self,x):
        self.x = x
    def d(self):
        pass

    
