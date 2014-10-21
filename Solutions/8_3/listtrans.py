# listtrans.py

class ListTransaction(object):
    def __init__(self,thelist):
        self.thelist = thelist
    def __enter__(self):
        self.working = list(self.thelist)
        return self.working
    def __exit__(self,type,val,tb):
        if type is None:
             # Commit the changes if no exceptions pending
             self.thelist[:] = self.working
        return False
