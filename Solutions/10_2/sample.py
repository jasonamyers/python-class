# sample.py

import ctypes

_sample = ctypes.cdll.LoadLibrary("./libsample.so")

isprime = _sample.isprime
isprime.argtypes=(ctypes.c_int,)
isprime.restype=ctypes.c_int

gcd = _sample.gcd
gcd.argtypes=(ctypes.c_int,ctypes.c_int)
gcd.restype=ctypes.c_int

cone_volume = _sample.cone_volume
cone_volume.argtypes=(ctypes.c_double,ctypes.c_double)
cone_volume.restype=ctypes.c_double

class Point(ctypes.Structure):
    _fields_ = [('x',ctypes.c_double),
                ('y',ctypes.c_double)]


distance = _sample.distance
distance.argtypes = (ctypes.POINTER(Point),
                     ctypes.POINTER(Point))
distance.restype = ctypes.c_double
