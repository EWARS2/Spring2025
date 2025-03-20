# Based on code I wrote sometime in 2021 to convert QR codes to NFOs.
# I should probably upload that project somewhere.

from PIL import Image
o = ""

def load(path_in):
    im = Image.open(path_in)
    return im, im.load()

def pront(s, end="\n"):
    global o
    o += str(s + end)

def format_no(path_in, end=""):
    im, pix = load(path_in)
    for y in range(im.height):
        for x in range(im.width):
            pront(pix[x, y], end=end)
        pront()

def format_lobit(path_in, l=None):
    if l is None:
        l = ['blue', 'yellow', 'red', 'brown']
    im, pix = load(path_in)
    for y in range(im.height):
        pront('<div class = "div-special">')
        for x in range(im.width):
            pront(f'<div class = "{l[pix[x,y]]}"></div>')
        pront("</div>")

def format_rgb(path_in):
    im, pix = load(path_in)
    for y in range(im.height):
        pront('<div class = "div-special">')
        for x in range(im.width):
            pront(f'<div style="background-color: rgb{pix[x,y]};"></div>')
        pront("</div>")

format_rgb("wiki_sample.png")

with open("o.txt", "w") as f:
    f.write(o)
    f.close()
