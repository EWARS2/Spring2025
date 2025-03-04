import re
def process(e, base=None):
    # Format
    e = e.capitalize()
    e = e.replace('X', '*')

    # Guess base if unspecified
    if base is None:
        if re.search(r"[2-9A-F]", e):
            base = 16
        else:
            base = 2

    # Generate eval expression and eval()
    e = e.split()
    for i in range(len(e)):
        if re.search(r"[A-F0-9]", e[i]):
            e[i] = "int(" + "'" + e[i] + "'" + ", base)"
    e = eval(" ".join(e))

    # Output
    print("Dec: ", e)
    print("Hex: ", hex(e))
    print("Bin: ", bin(e))


process('319',10)