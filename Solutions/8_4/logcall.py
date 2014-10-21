# logcall.py

import logging
import os
from functools import wraps
import collections

def logged(func):
    # If logging not enabled, return the original function unwrapped
    if 'LOGDISABLE' in os.environ:
        return func
    print("Adding logging to", func.__name__)
    log = logging.getLogger(func.__module__)
    @wraps(func)
    def wrapper(*args,**kwargs):
        log.debug("%s", func.__name__)
        return func(*args,**kwargs)
    return wrapper

def loglevel(level):
    def decorate(func):
        print("Adding logging to", func.__name__)
        log = logging.getLogger(func.__module__)
        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level, "%s", func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorate

def logmethods(cls):
    for key, value in cls.__dict__.items():
        if isinstance(value, collections.Callable):
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








        
