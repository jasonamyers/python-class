# portfolio.py

class Portfolio(object):
    def __init__(self):
        self._stocks = []    # Internal list
    def totalcost(self):
        return sum(s.shares*s.price for s in self._stocks)
    def __getattr__(self,name):
        return getattr(self._stocks,name)
    def __len__(self):
        return len(self._stocks)
    def __getitem__(self,index):
        return self._stocks[index]

# Example
if __name__ == '__main__':
    from stock import Stock
    p = Portfolio()
    p.append(Stock('GOOG',100,490.1))
    p.append(Stock('IBM',50,91.5))
    p.insert(0,Stock('AA',25,24.55))
    print len(p)
    print p[1]

    
    
    
