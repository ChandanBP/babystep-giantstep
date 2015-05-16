
from random import randint
from bisect import bisect_left

def value_exists(needle, haystack):
    # finds if needle exists in haystack of tuples and returns it if so
    if needle in haystack:
	    return haystack[needle], needle

n = 200000
size = 10000000000
     # 10000000000

# fill array A with random numbers
arrayA = [1]
for i in range(1, n):
    arrayA.append(randint(0, size))

arrayA = sorted(arrayA)

dictA = {}
for idx, num in enumerate(arrayA):
	dictA[num] = idx

# search
for i in range(1, n):
    check = value_exists(randint(0, size), arrayA)
    if check:
        break

print(check)
