# sample.py

from logcall import logged, loglevel
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
