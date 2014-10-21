import logging
log = logging.getLogger(__name__)
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split()
        try:
            record = {
                'name': fields[0],
                'shares': int(fields[1]),
                'price': float(fields[2])
            }
            portfolio.append(record)
        except ValueError as e:
            log.warning('Warning: Couldn\'t parse: %r', line)
            log.debug('Reason: %s' % e)
    return portfolio
