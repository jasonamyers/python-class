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
        return r
    return wrapper

class timeblock(object):
    def __init__(self, label):
        self.label = label
    def __enter__(self):
        self.start = time.time()
    def __exit__(self,type,val,tb):
        end = time.time()
        print(self.label, ':', end-self.start)
        return False
