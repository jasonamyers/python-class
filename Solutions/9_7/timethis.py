# timethis.py
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
    return wrapper

class timeblock(object):
    def __init__(self,name):
        self.name = name
    def __enter__(self):
        self.start = time.time()
    def __exit__(self,type,val,tb):
        end = time.time()
        print(self.name,":",end-self.start)
        return False
    
# Reimplemented version using generators
from contextlib import contextmanager

@contextmanager
def timeblock(name):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(name,":",end-start)



