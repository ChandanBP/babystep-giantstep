#
# MKY assigment 3 Babystep-Giantstep alg
#

from functions import *
import math

mod = 113
order = 112
g = 3
h = 57  # looking for (3^? = 57 mod 113) which is (log3 57 = ? mod 113)

a = 2 >> 1;
print(bin(a))
exit()

n = math.ceil(math.sqrt(mod)) # n = 11

mults = [1]

for i in range(1, n):
    mults.append(mult(mults[i-1], g, mod))
mults = enumerate(mults)

mults = sorted(mults, key=lambda x: x[1])

for i in mults:
    print(i)

# tmp = power(tmp, n, mod)  # 58
# todo: throw away all previous results
# tmp = power(tmp, n, mod); // 58
# arrayB[0] = h;
# for (int i = 1; i < n; ++i)
# {
	# arrayB[i] = mult(arrayB[i-1], tmp, mod);
# }
