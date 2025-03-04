"""
Retrieved from here:
https://stackoverflow.com/questions/1604464/twos-complement-in-python
"""
def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

binary_string = '11111111'
o = twos_comp(int(binary_string,2), 8)
# o = twos_comp(int('0xFFFFFFFF',16), 32)
print("Dec: ", o)
print("Hex: ", hex(o))
print("Bin: ", bin(o))
