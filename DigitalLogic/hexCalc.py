"""
Two's Complement from here:
https://stackoverflow.com/questions/16255496/format-negative-integers-in-twos-complement-representation
"""
import re
def process(f, base=None):
    # Format
    f = f.upper()
    f = f.replace('X', '*')

    # Guess base if unspecified
    if base is None:
        if re.search(r"[2-9A-F]", f):
            base = 16
        else:
            base = 2

    # Generate eval expression and eval()
    f = f.split()
    for i in range(len(f)):
        if re.search(r"[A-F0-9]", f[i]):
            f[i] = "int(" + "'" + f[i] + "'" + ", base)"
    f = eval(" ".join(f))

    # Output
    print("\nOne's Complement")
    print("Dec: ", f)
    print("Hex: ", hex(f))
    print("Bin: ", bin(f))
    print("\nTwo's Complement")
    print("Dec: ", f)
    print("Hex: ", hex(f % (1 << 8)))
    print("Bin: ", bin(f % (1 << 8)))

process('-108', 10)
process('FF + FF')
