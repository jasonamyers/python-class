# timethis.py
import time
from functools import wraps
from contextlib import contextmanager


def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return r
    return wrapper


@contextmanager
def timeblock(name):
    start = time.time()
    yield
    end = time.time()
    print(name, ':', end-start)
