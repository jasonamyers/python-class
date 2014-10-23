import logging
import os
from functools import wraps

log = logging.getLogger(__name__)

def logged(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        log.debug('%s:%s', func.__module__, func.__name__)
        return func(*args,**kwargs)
    return wrapper

def loglevel(level=logging.DEBUG):
    def makewrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, '%s:%s', func.__module__, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return makewrapper


def logmethods(cls):
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls,key,logged(value))
    return cls


def loggetattribute(cls):
    old_getattribute = cls.__getattribute__
    log = logging.getLogger(cls.__name__)
    def new_getattribute(self,name):
        log.debug("Accessing %s", name)
        return old_getattribute(self,name)
    cls.__getattribute__ = new_getattribute
    return cls

