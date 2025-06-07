import os
from time import sleep


# 25 lines by 80 characters


def display(directory="frames"):
    for filename in sorted(os.listdir(directory)):
        f = os.path.join(directory, filename)
        with open(f, 'r') as file:
            print(file.read(), end="\r", flush=True)


def generate():
    file = open("output.txt", "w")
    s = ''
    for i in range(80):
        s += "#"
    s += "\n"
    for i in range(25):
        file.write(s)
    file.close()

#display()
generate()