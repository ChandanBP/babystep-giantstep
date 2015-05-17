#
# MKY assigment 3 Babystep-Giantstep alg
# help functions
# multiplication and adding in GF(2^35)
#

def print_bin(number):
    # prints number in binary format of length 40
    print(format(number, '040b'))


def print_hex(number):
    # prints number in hex format
    print(hex(number))


def lfsr(number):
    # implements the Linear feedback shift register which computes A = Ax mod f
    # see BHW lecture 5, slide 20
    x34 = number & (1 << 34)
    x32 = number & (1 << 32)
    x34 >>= 34
    x32 >>= 32
    x33 = x34 ^ x32
    x33 <<= 33

    number <<= 1
    tmp = number & 0xfdffffffff  # destroys x^33 bit
    number = tmp | x33

    # x34 is shifted to x^0
    # no need for destroying here because the bit is always 0 due to the shift
    number |= x34
    # 1. bit ever needs to be destroyed, shift could move 1 in here
    number &= 0xf7ffffffff
    return number


def mult(a, b):
    # multiplies a * b using double-and-add algorithm
    result = 0
    tmp = 1 << 35

    for i in range(0, 36):
        if b & tmp:
            result = add(result, a)

        if i != 35:
            result = lfsr(result)

        tmp = tmp >> 1

    return result


def add(a, b):
    # adds a + b
    return a ^ b
