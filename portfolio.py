class Portfolio(object):

    def __init__(self):
        self._stocks = []

    def __getattr__(self, name):
        return getattr(self._stocks, name)

    def totalcost(self):
        return sum(s.shares *s.price for s in self._stocks)
