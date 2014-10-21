# optimize.py
import time

import math
def foo_1(xpts):
    ypts = [2*math.sin(x) for x in xpts]
    return ypts

from math import sin
def foo_2(xpts):
    ypts = [2*sin(x) for x in xpts]
    return ypts

def foo_3(xpts):
    from math import sin
    ypts = [2*sin(x) for x in xpts]
    return ypts

def timefunc(func,xpts):
    start = time.time()
    ypts = func(xpts)
    end = time.time()
    print(end-start)

xpts = range(10000000)
timefunc(foo_1,xpts)
timefunc(foo_2,xpts)
timefunc(foo_3,xpts)
