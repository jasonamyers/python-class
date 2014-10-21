# dateobj.py
import time

class Date(object):
    datefmt = "{date.month}/{date.day}/{date.year}"
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return self.datefmt.format(date=self)

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def from_timestamp(cls, ts):
        t = time.localtime(ts)
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

class ISODate(Date):
    datefmt = '{date.year}-{date.month:02d}-{date.day:02d}'
    
# Here's a test to try with the ISODate class
if __name__ == '__main__':
    d = ISODate.today()
    print(d)
    
    e = Date.today()
    print(e)

    

    
