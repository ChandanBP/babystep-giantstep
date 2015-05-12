#
# MKY assigment 3 Babystep-Giantstep alg
#
# finalResult = 0x6634633308


from gf import *
import math

def value_exists(needle, haystack):
	# finds if needle exists in haystack of tuples and returns it if so
	for item in haystack:
		if item[1] > needle:
			return None
		if item[1] == needle:
			return item


order = 2**35
g = 0x0000000002
h = 0x05C8683CCC
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

# ##### PART 2 ##### #
print("starting part 2")

print("starting search")

# zero cycle:
lastPower = 1
value = h
for i in range(1, n):
    lastPower = mult(lastPower, balloon)
    value = mult(h, lastPower)
    check = value_exists(value, arrayA)
    if check:
        break

finalResult = check[0] + i * n

print(finalResult)
