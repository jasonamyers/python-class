class Structure(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Expected %d arguments" % len(self._fields))
        for name,arg in zip(self._fields, args):
            setattr(self, name, arg)
        for name,arg in kwargs.items():
            if hasattr(self, name):
                raise TypeError("Argument %s duplicated" % name)
            if name not in self._fields:
                raise TypeError("Unknown argument %s" % name)
            setattr(self, name, arg)
        if not all(hasattr(self, name) for name in self._fields):
            missing = self._fields - vars(self).keys()
            raise TypeError("Missing argument(s) %s" % ','.join(missing))

