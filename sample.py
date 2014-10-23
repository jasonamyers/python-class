from logcall import loglevel, logmethods, loggetattribute
import logging

@loglevel()
def a():
    pass

@loglevel(logging.WARNING)
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
