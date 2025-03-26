"""
Take clipboard data from the C64 emulator VICE,
and convert shifted graphics text into plain ASCII.

Using to make mockups of C64 demos on other platforms.
Mostly using stuff by GOTO80, such as Birds on Fire.
"""

def remove_c64(s):
    d = {
        'V': 'X',
        'N': '/',
        'M': '\\',
        'C': '-',
        'D': '-',
        'B': '|',
    }

    for i in d:
        s = s.replace(i, d[i])
    return s.upper()


path = "in.txt"
with open(path, "r", errors='ignore') as f:
    text = f.read()
    o = remove_c64(text)
    print(o)
#with open("o.txt", "w", errors='ignore') as f:
#    f.write(o)

