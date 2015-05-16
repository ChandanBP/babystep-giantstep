
from random import randint
from bisect import bisect_left

def value_exists(needle, haystack):
	# finds if needle exists in haystack of tuples and returns it if so
	i = bisect_left(haystack, needle)
	return i != len(haystack) and haystack[i] == needle
	# for item in haystack:
		# if item[1] > needle:
			# return None
		# if item[1] == needle:
			# return item

n = 200000
size = 100000000
#size = 10000000000

arrayA = [1]
for i in range(1, n):
    arrayA.append(randint(0, size))

print("arrayA created")

arrayA = enumerate(arrayA)
print("arrayA enumerated")

arrayA = sorted(arrayA, key=lambda x: x[1])
print("arrayA sorted")

for i in range(1, n):
    value = randint(0, size)
    check = value_exists(value, arrayA)
    if check:
        break

print("done")
print(check)

#if check:
#	print(check[0])
