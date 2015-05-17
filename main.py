#
# MKY assigment 3 Babystep-Giantstep alg
# finalResult = 0x04658ca487
# Tomas Susanka
#

from gf import *
import math
from bisect import bisect_left

def value_exists(needle, haystack, values):
    # finds if needle exists in haystack of tuples and returns it if so
    i = bisect_left(values, needle)
    if i != len(values) and values[i] == needle:
        return haystack[i]
    else:
        return None


order = 2**35 - 1
g = 0x0000000002
h = 0x05c8683cce
n = math.ceil(math.sqrt(order))
inverse = 0x0500000000  # g^-1
multiplier = 0x038ab9deae # inverse^n

# creates list of g^i values
array = [1]
for i in range(1, n):
    array.append(mult(array[i-1], g))

# sorts array but preservers indexes
array = enumerate(array)
array = sorted(array, key=lambda x: x[1])

# moves all values into seperate array, so binary search can be conducted
values = [item[1] for item in array]

# creates h*g^{-in} and searches for that value in array right away
lastPower = 1
value = h
for i in range(1, n):
    lastPower = mult(lastPower, multiplier)
    value = mult(h, lastPower)
    check = value_exists(value, array, values)
    if check:
        break

# when found x = j+in:
finalResult = check[0] + i * n
print_hex(finalResult)
