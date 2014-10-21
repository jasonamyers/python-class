class Date(object):

    datefmt = '{date.month}/{date.day}/{date.year}'

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return self.datefmt.format(date=self)

    def __repr__(self):
        return '%s(%r, %r, %r)' % (self.__class__.__name__, self.year, self.month, self.day)

    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        if not isinstance(other, Date):
            raise ValueError('Not comparing two dates')
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other):
        if not isinstance(other, Date):
            raise ValueError('Not comparing two dates')
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)

    def __gt__(self, other):
        if not isinstance(other, Date):
            raise ValueError('Not comparing two dates')
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __ge__(self, other):
        if not isinstance(other, Date):
            raise ValueError('Not comparing two dates')
        return (self.year, self.month, self.day) => (other.year, other.month, other.day)

    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        self = cls.__new__(cls)
        self.year = t.tm_year
        self.month = t.tm_mon
        self.day = t.tm_mday
        return self

    @classmethod
    def from_timestamp(cls, unix):
        import time
        t = time.localtime(unix)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


class ISODate(Date):
    pass
