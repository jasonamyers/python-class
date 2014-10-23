class Profiled(object):
    def __init__ (self, func):
        self._func = func
        self.calls = 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self._func(*args, **kwargs)
