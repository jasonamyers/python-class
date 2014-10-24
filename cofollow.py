import os
import time

# Data source
def follow(filename, target):
    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)

# Decorator for coroutine functions
def coroutine(func):
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f
    return start

# Sample coroutine
@coroutine
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print("%(name)10s %(price)10.2f %(change)10.2f" % item)

@coroutine
def splitter(target):
     while True:
         line = yield
         target.send(line.split(','))

@coroutine
def make_records(names,target):
    while True:
        fields = yield
        record = dict(zip(names,fields))
        target.send(record)

@coroutine
def unquote(keylist,target):
    while True:
        record = yield
        for key in keylist:
            record[key] = record[key].strip('"')
        target.send(record)

@coroutine
def convert(converter,keylist,target):
    while True:
        record = yield
        for key in keylist:
            record[key] = converter(record[key])
        target.send(record)

if __name__ == '__main__':
    output = printer()
    make_float = convert(float,['price','change','open','high','low'], output)
    make_int = convert(int,['volume'], make_float)
    quote_fixer = unquote(["name","date","time"], make_int)
    records = make_records(['name','price','date','time', 'change','open','high','low','volume'], quote_fixer)
    rows = splitter(records)
    follow("Data/stocklog.dat", rows)

