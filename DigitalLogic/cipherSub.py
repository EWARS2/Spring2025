# WIP
OG = 'ABCD EFGH  IJKL MNOP QRST UVWX YZ01 2345 6789'
REMAP = '2BQF 5WRT D8IJ 6HLC OSUV K3A0 X9YZ N1G4 ME7P'

def clean(og, remap):
    og = og.replace(' ', '')
    remap = remap.replace(' ', '')
    print(og)
    print(remap)
    return og, remap, ''

def encode(s, remap=REMAP, og=OG):
    og, remap, o = clean(og, remap)
    for i in s:
        o += remap[og.index(i)]
    return o

def decode(s, remap=REMAP, og=OG):
    og, remap, o = clean(og, remap)
    for i in s:
        o += og[remap.index(i)]
    return o


print(decode("T5JC65"))
