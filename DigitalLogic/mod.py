def parse(s, mod):
    s = s.upper()
    s = s.replace('X', '*')
    print(s)
    print(eval(s))
    print(eval(s) % mod)

parse("85 x 102 ", 257)