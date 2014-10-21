# cofollow.py
import os
import time

def follow(filename,target):
    with open(filename,"r") as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)

# Decorator for coroutines
def coroutine(func):
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        next(f)
        return f
    return start

# Sample coroutine
@coroutine
def printer():
    while True:
        item = yield
        print(item)

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


# Example use.   Here, a pipeline is setup, but the components
# have to initialized in reverse order.  It look weird, but try
# wrap your mind around it.

if __name__ == '__main__':
    t_printer = printer()         # This is the very end of the pipeline
    t_convert_int = convert(int, ['volume'], t_printer)
    t_convert_float = convert(float, ['price','change','open','high','low'], t_convert_int)
    t_unquote = unquote(['name','date','time'],t_convert_float)
    t_records = make_records(['name','price','date','time','change','open','high','low','volume'], t_unquote)
    t_splitter = splitter(t_records)
    follow("../../Data/stocklog.dat",t_splitter)      

# Example use (Mondo edition)
if __name__ == '__main__':
    follow("../../Data/stocklog.dat",
           splitter(
           make_records(['name','price','date','time','change','open','high','low','volume'],
           unquote(['name','date','time'],
           convert(float,['price','change','open','high','low'],
           convert(int,['volume'],
           printer()
           ))))))
