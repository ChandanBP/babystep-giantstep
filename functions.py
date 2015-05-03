#
# MKY assigment 3 Babystep-Giantstep alg
# help functions
#
import subprocess


def power(num, power, mod):
    # Calculates $num^$power mod $mod
    if power == 0:
        return 1
    result = 1
    for i in range(power):
        result = (result * num) % mod
    return result


def mult(a, b, mod):
    a = a * b
    return a % mod


def add(a, b, mod):
    return (a + b) % mod


def value_exists(needle, haystack):
    return [item for item in haystack if item[1] == needle]


def gf_power(num, power):
    if power == 0:
        return 1
    result = 1
    for i in range(power):
        result = gf_mult(result, num)
    return result


def gf_mult(a, b):
    cmd = "./multiplicator " + format(a, '02x').zfill(10) + " " + format(b, '02x').zfill(10)
    output = subprocess.getoutput(cmd)
    return int(output, 16)


def gf_add(a, b):
    return a ^ b
