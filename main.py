#
# MKY assigment 3 Babystep-Giantstep alg
#

from functions import *
import math

mod = 113
order = 112
g = 3
h = 57  # looking for (3^? = 57 mod 113) which is (log3 57 = ? mod 113)
n = math.ceil(math.sqrt(mod)) # n = 11
inverse = 38 # 3^-1

arrayA = [1]

for i in range(1, n):
    arrayA.append(mult(arrayA[i-1], g, mod))
arrayA = enumerate(arrayA)

arrayA = sorted(arrayA, key=lambda x: x[1])

# ##### PART 2 ##### #

balloon = power(inverse, n, mod)  # 58

# zero cycle:
lastPower = 1
value = h
for i in range(1, n):
    lastPower = mult(lastPower, balloon, mod)
    value = mult(h, lastPower, mod)
    check = valueExists(value, arrayA)
    if check:
        break

finalResult = check[0][0] + i * n

print(finalResult)
print("log", g, " of ", h, " is ", finalResult, sep="")
print("Checking if ", g, "^", finalResult, " = ", h, ":", sep="")
if power(g, finalResult, mod) == h:
    print("Check valid")
else:
    print("Check failed, something is wrong")
