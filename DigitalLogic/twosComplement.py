"""
Original function from here:
https://stackoverflow.com/questions/1604464/twos-complement-in-python
"""
def twos_comp(val, bits=8):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value

    # return positive value as is
    print("Dec: ", val)
    print("Hex: ", hex(val))
    print("Bin: ", bin(val))

#twos_comp(-108)
#twos_comp(108)
#twos_comp(int('10000000',2))
# o = twos_comp(int('0xFFFFFFFF',16), 32)
