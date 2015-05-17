#
# MKY assigment 3 Babystep-Giantstep alg
#
# finalResult = 0x04658ca487


from gf import *
import math
from bisect import bisect_left


def value_exists(needle, haystack, keys):
    # finds if needle exists in haystack of tuples and returns it if so
    i = bisect_left(keys, needle)
    if i != len(keys) and keys[i] == needle:
        return haystack[bisect_left(keys, needle)]
    else:
        return None


order = 2**35 - 1
g = 0x0000000002
h = 0x05c8683cce
n = math.ceil(math.sqrt(order))
inverse = 0x0500000000  # g^-1
balloon = 0x038ab9deae

print("n is", n)

print("creating arrayA")
arrayA = [1]
for i in range(1, n):
    arrayA.append(mult(arrayA[i-1], g))

print("enumerating arrayA")
arrayA = enumerate(arrayA)

print("sorting arrayA")
arrayA = sorted(arrayA, key=lambda x: x[1])

print("getting keys")
keys = [item[1] for item in arrayA]  # precomputed list of keys

# ##### PART 2 ##### #
print("starting part 2")

print("starting search")

# zero cycle:
lastPower = 1
value = h
for i in range(1, n):
    lastPower = mult(lastPower, balloon)
    value = mult(h, lastPower)
    check = value_exists(value, arrayA, keys)
    if check:
        break

finalResult = check[0] + i * n
print_hex(finalResult)
