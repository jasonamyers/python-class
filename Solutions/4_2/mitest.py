# mitest.py

class Base(object):
    def __init__(self,opt=None):
        print("Base.__init__")

class A(Base):
    def __init__(self):
        print("A.__init__")
        Base.__init__(self)
#        super(A,self).__init__()
#        super(A,self).__init__(42)
class B(Base):
    def __init__(self):
        print("B.__init__")
        Base.__init__(self)
#        super(B,self).__init__()

    
class C(A,B):
    def __init__(self):
        print("C.__init__")
        A.__init__(self)
        B.__init__(self)
#        super(C,self).__init__()


