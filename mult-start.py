
# uint8_t pattern[8] = {0x80,0x40,0x20,0x10,0x08,0x04,0x02,0x01};


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


def gf_mult(a, b):
    result = 0
    tmp = 1 << 36  # or something like that

    for i in range(0, 36):
        if b & tmp:
            result = gf_add(result, a)

        lfsr(result)

        tmp = tmp >> 1

    # result = result & ~(1 << 35); # destroys 1 bit
    return result


def gf_add(a, b):
    # delete first bit?
    return a ^ b

# first highest is 0x07 !!!!
print_hex(lfsr(0x0400fff201))

# print(gf_mult(0x12, 0x01))
