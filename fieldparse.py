def parse(lines, conversions, names):
    results = []
    for line in lines:
        results.append({name: func(val) for name, func, val in zip(names, conversions, line.split())})
    return results
