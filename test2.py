
from random import randint
from bisect import bisect_left

def value_exists(needle, haystack):
    # finds if needle exists in haystack of tuples and returns it if so
	i = bisect_left(haystack, needle)
	return i != len(haystack) and haystack[i] == needle

n = 200000
size = 100

# fill array A with random numbers
arrayA = [1]
for i in range(1, n):
    arrayA.append(randint(0, size))
arrayA = enumerate(arrayA)
# sort them by values keeping its indexes
arrayA = sorted(arrayA, key=lambda x: x[1])

# search
for i in range(1, n):
    value = randint(0, size)
    check = value_exists(value, arrayA)
    if check:
        break

print(check)
