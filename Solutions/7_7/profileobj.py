# profileobj.py

# A simple version (for parts a-b)
import types
class Profiled(object):
    def __init__(self,func):
        self.func = func
        self.ncalls = 0
    def __call__(self,*args,**kwargs):
        self.ncalls +=1
        return self.func(*args,**kwargs)
    def __get__(self,obj,cls=None):
        return types.MethodType(self,obj,cls)

# A modified version for part c (change False to True to enable)
if False:
    class Profiled(object):
        def __init__(self,func):
            self.func_type = type(func)
            if isinstance(func,(staticmethod,classmethod)):
                func = func.__func__
            self.func = func
            self.ncalls = 0
        def __call__(self,*args,**kwargs):
            self.ncalls +=1
            return self.func(*args,**kwargs)
    
        def __get__(self,obj,cls=None):
            if self.func_type is staticmethod:
                return self
            elif self.func_type is classmethod:
                return types.MethodType(self,cls,cls)
            else:
                return types.MethodType(self,obj,cls)

# sample use
if __name__ == '__main__':
    def add(x,y):
        return x+y

    add = Profiled(add)
    print(add(2,3))
    print(add("hello","world"))
    print(add.ncalls)

    class Foo(object):
        def a(self):
            "This is an example of an instance method"
            print("Instance method")
        a = Profiled(a)

    f = Foo()
    f.a()
    Foo.a(f)
    print(Foo.a.ncalls)
            
    
    
    
