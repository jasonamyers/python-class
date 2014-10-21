# rpc.py

import inspect
import cgi

class RPCDispatcher(object):
    def __init__(self):
        self.handlers = {}

    def register_function(self,func):
        '''Register a function with the dispatcher'''
        url = getattr(func,"url",func.__name__)
        func.argnames = inspect.getargspec(func).args
        self.handlers[url] = func

    def call(self,url,parms):
        '''Given a url and query string, dispatch to a function'''
        func = self.handlers[url]
        raw_parms = cgi.parse_qs(parms)
        converted_parms = [ctype(raw_parms[pname][0])
                           for ctype,pname in zip(func.argtypes,func.argnames)]
        return func(*converted_parms)

# Example
if __name__ == '__main__':
    # Define some function to expose
    def add(x,y):
        return x+y
    add.url = "funcs/add"
    add.argtypes = (int,int)

    def sub(x,y):
        return x-y
    sub.url = "funcs/sub"
    sub.argtypes = (int,int)

    # Create the dispatcher
    dispatcher = RPCDispatcher()
    dispatcher.register_function(add)
    dispatcher.register_function(sub)

    # Try some sample calls
    print(dispatcher.call("funcs/add","x=4&y=5"))
    print(dispatcher.call("funcs/sub","x=4&y=5"))
#    print(dispatcher.call("funcs/sub","x=4&y=a"))     # Uncomment for a ValueError

    
        
        
        
        
        
