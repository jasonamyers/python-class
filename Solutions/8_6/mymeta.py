# mymeta.py

class mytype(type):
    def __new__(cls,name,bases,__dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__.keys()))
        return type.__new__(cls,name,bases,__dict__)

class myobject(metaclass=mytype):
    pass
