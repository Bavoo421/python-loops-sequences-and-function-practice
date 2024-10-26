def even_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)

even_keys({'a': 2, 'b': 3, 'c': 4})
