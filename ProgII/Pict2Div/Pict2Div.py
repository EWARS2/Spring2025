# Based on code I wrote sometime in 2021 to convert QR codes to NFOs.
# I should probably upload that project somewhere.

from PIL import Image #For opening images
im = Image.open("markus.png")
pix = im.load()

def insert(n):
    l = ['blue', 'yellow', 'red', 'brown']
    return f'<div class = "{l[n]}"></div>'

for y in range(im.height):
    print('<div class = "div-special">')
    for x in range(im.width):
        print(insert(pix[x,y]))
    print("</div>")
