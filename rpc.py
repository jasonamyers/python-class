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
