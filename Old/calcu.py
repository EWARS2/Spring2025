base = 16
a = "FFFF"
b = "FF"
a = int(a, base)
b = int(b, base)
o = a + b

print("Dec: ", o)
print("Hex: ", hex(o))
print("Bin: ", bin(o))