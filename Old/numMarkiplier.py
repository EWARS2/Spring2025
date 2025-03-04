# WIP Hex calculator by Ethan Reed, 2025/3/3
# Intended to support arbitrary numbering systems, case-sensitive.
# If you're in a pinch: https://www.rapidtables.com/calc/math/hex-calculator.html
# Problem with RapidTables though, is they lack a Binary and an Octal calculator.
# That's what this script intends to rectify on its own.

SYMS_BIN = '01'
SYMS_DEC = '0123456789'
SYMS_HEX = '0123456789ABCDEF'
SYMS_OCT = '01234567'

def process(i1, i2, syms):
    # So we can work from left to right:
    i1 = i1[::-1]  # Reverse string
    i2 = i2[::-1]  # Reverse string

    # Pad numbers with zeros
    if len(i1) > len(i2):
        for i in range(len(i1) - len(i2)):
            i2 += syms[0]
    else:
        for i in range(len(i1) - len(i2)):
            i1 += syms[0]

    # Pad extra zero for overflow
    i1 += syms[0]
    i2 += syms[0]

    return i1, i2, 0, ''

def add(i1, i2, syms=SYMS_HEX):
    i1, i2, carry, o = process(i1, i2, syms)
    for i in range(len(i1)):
        d1 = syms.index(i1[i])
        d2 = syms.index(i2[i])
        d = d1 + d2 + carry
        carry = 0
        if d >= len(syms):
            carry = 1
            d -= len(syms)
        o += syms[d]
    return o[::-1] # Reverse string





print(add('FFFF', 'FF'))
print(add('0101', '1010', SYMS_BIN))

