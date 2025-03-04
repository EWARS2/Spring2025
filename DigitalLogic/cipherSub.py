# WIP
OG  = 'ABCD EFGH  IJKL MNOP QRST UVWX YZ01 2345 6789'
MAP = ' 2BQF 5WRT D8IJ 6HLC OSUV K3A0 X9YZ N1G4 ME7P'

def clean():
    og = OG.replace(' ', '')
    remap = MAP.replace(' ', '')

def encode(s, remap=MAP, og=OG):
    o = ''
    for i in s:
        o += remap[og.index(i)]
    return o



print(og)
print(map)
