
def print_bin(number):
    print(format(number, '040b'))


def print_hex(number):
    print(hex(number))


def lfsr(number):

    x34 = number & (1 << 34)
    x32 = number & (1 << 32)
    x34 >>= 34
    x32 >>= 32
    x33 = x34 ^ x32
    x33 <<= 33

    number <<= 1

    tmp = number & 0xfdffffffff  # destroys x^33 bit nonw: ~(1 << 32)

    number = tmp | x33

    # x34 is shifted to x^0
    # no need for destroying here because the bit is always 0 due to the shift
    number |= x34

    # 1. bit ever needs to be destroyed, shift could move 1 in here
    number &= 0xf7ffffffff

    return number


def mult(a, b):
    result = 0
    tmp = 1 << 35  # or something like that

    for i in range(0, 36):
        if b & tmp:
            result = add(result, a)

        if i != 35:
            result = lfsr(result)

        tmp = tmp >> 1

    # result = result & ~(1 << 35); # destroys 1 bit
    return result


def add(a, b):
    # delete first bit?
    return a ^ b
