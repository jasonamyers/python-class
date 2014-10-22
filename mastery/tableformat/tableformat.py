def old_print_table(objects,attributes):
    lengths = {}
    fmts = {}
    header = ''
    for attr in attributes:
        attrlen = len(str(attr))

        lengths[attr] = max([max([len(str(getattr(thing, attr, 'undef'))) for thing in objects]), len(str(attr))]) + 2
        print('{:>{width}}'.format(attr, width=lengths[attr]), end=' ')
    print()
    for attr in attributes:
        print('-' * lengths[attr] + ' ', end=' ')
    print()
    for obj in objects:
        for attr in attributes:
            print('{:>{width}}'.format(getattr(obj, attr, 'undef'), width=lengths[attr]), end=' ')
        print()
