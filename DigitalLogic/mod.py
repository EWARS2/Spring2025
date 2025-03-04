def parse(s, mod):
    s = s.upper()
    s = s.replace('X', '*')
    s = s.replace('^', '**')
    print(s)
    print(eval(s))
    print(eval(s) % mod)

parse("3 ^ 4", 15)