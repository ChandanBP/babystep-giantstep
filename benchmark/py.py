#
# MKY assigment 3 benchmark
#

a = 12354;
b = 52529;

for x in range(0,100000000):
    a = (a * b) % 1000000

print(a)

