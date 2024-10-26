def keys_greater_than_n(d, n):
    return [key for key, value in d.items() if value > n]

print(keys_greater_than_n({'a': 5, 'b': 12, 'c': 3}, 4))
