"""
Take clipboard data from the C64 emulator VICE,
and convert shifted graphics text into plain ASCII.

Using to make mockups of C64 demos on other platforms.
Mostly using stuff by GOTO80, such as Birds on Fire.
"""

def multi_replace(s, d):
    for i in d:
        s = s.replace(i, d[i])
    return s


caps = {
    '.': '\\',
    'V': 'X',
    'N': '/',
    'M': '\\',
    'C': '-',
    'D': '-',
    'B': '|',
    'I': '/',
    'E': '[',
    'F': '#',
    'T': ']',
    'L': '.',
    'P': '7',
    'Z': 'J',
}

bowdown3_test = {
    'a': ' ',
    'c': ' ',
    'b': ' ',
    'A': '/',
    'C': '/',
    'B': '#'
}

path = "in.txt"
with open(path, "r", errors='ignore') as f:
    text = f.read()
    o = multi_replace(text, bowdown3_test)
    o = o.upper()
    print(o)
#with open("o.txt", "w", errors='ignore') as f:
#    f.write(o)
