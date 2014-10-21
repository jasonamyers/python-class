class Date(object):

    datefmt = '{date.month}/{date.day}/{date.year}'

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return self.datefmt.format(date=self)

    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def from_timestamp(cls, unix):
        import time
        t = time.localtime(unix)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
