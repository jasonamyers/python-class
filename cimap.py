class CIMap(dict):
    '''
    Case insensitive map
    '''
    def __getitem__(self, key):
        return super(CIMap, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        super(CIMap, self).__setitem__(key.lower(), value)

    def __delitem__(self, key):
        super(CIMap, self).__delitem__(key.lower())


class CIMixin(object):
    def __getitem__(self, key):
        return super(CIMixin, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        super(CIMixin, self).__setitem__(key.lower(), value)

    def __delitem__(self, key):
        super(CIMixin, self).__delitem__(key.lower())

class LoggedMapMixin(object):
    def __getitem__(self, key):
        item = super(LoggedMapMixin, self).__getitem__(key.lower())
        print('getitem: %s %s' % (key, item))
        return item

    def __setitem__(self, key, value):
        print('setitem: %s %s' % (key, value))
        super(LoggedMapMixin, self).__setitem__(key.lower(), value)

    def __delitem__(self, key):
        print('delitem: %s' % (key))
        super(LoggedMapMixin, self).__delitem__(key.lower())
