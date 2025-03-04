# WIP
OG  = 'ABCD EFGH  IJKL MNOP QRST UVWX YZ01 2345 6789'
MAP = ' 2BQF 5WRT D8IJ 6HLC OSUV K3A0 X9YZ N1G4 ME7P'

def encode(s, map=MAP, og=OG):
    o = ''
    for i in s:
        o += map[og.index(i)]
    return o

og = og.replace(' ', '')
remap = remap.replace(' ', '')

print(og)
print(map)
