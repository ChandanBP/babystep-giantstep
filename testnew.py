
from bisect import bisect_left

data = [(0, 1), (5, 3), (7, 4), (9, 5), (3, 8), (8, 9), (4, 10)]

data.sort(key=lambda r: r[1])

keys = [r[1] for r in data]  # precomputed list of keys

def value_exists(needle, haystack, keys):
    # finds if needle exists in haystack of tuples and returns it if so
    i = bisect_left(keys, needle)
    if i != len(keys) and keys[i] == needle:
        return haystack[bisect_left(keys, needle)]
    else:
        return None

print(value_exists(10, data, keys))
