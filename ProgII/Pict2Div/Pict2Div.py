# Based on code I wrote sometime in 2021 to convert QR codes to NFOs.
# I should probably upload that project somewhere.

from PIL import Image


def load(path):
    im = Image.open(path)
    return im, im.load()

def format_no(path, end=""):
    im, pix = load(path)
    for y in range(im.height):
        for x in range(im.width):
            print(pix[x, y], end=end)
        print()

def format_lobit(path, l=None):
    if l is None:
        l = ['blue', 'yellow', 'red', 'brown']
    im, pix = load(path)
    for y in range(im.height):
        print('<div class = "div-special">')
        for x in range(im.width):
            print(f'<div class = "{l[pix[x,y]]}"></div>')
        print("</div>")

def format_rgb(path):
    im, pix = load(path)
    for y in range(im.height):
        print('<div class = "div-special">')
        for x in range(im.width):
            print(f'<div style="background-color: rgb{pix[x,y]};"></div>')
        print("</div>")

format_rgb("wiki_sample.png")
