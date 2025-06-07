import os
import random
import keyboard
from time import sleep


# 25 lines by 80 characters

HOME_CHAR = "\033[H"

def display(directory="frames"):
    print(HOME_CHAR)
    while True:
        for filename in sorted(os.listdir(directory)):
            f = os.path.join(directory, filename)
            with open(f, 'r') as file:
                print(file.read(), end=HOME_CHAR, flush=True)


def generate():
    file = open("output.txt", "w")
    chars=['\\', '/']
    #chars=['#']
    for i in range(24):
        s = ''
        for i in range(79):
            s += random.choice(chars)
        s += "\n"
        file.write(s)
    file.close()

#generate()
display()
