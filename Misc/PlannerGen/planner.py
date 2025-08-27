# Unfinished

import csv
import os

def generate(directory="./"):
    for filename in sorted(os.listdir(directory)):
        f = os.path.join(directory, filename)
        if filename.lower().endswith(".csv"):
            print(f)

            with open(f, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)

            for i in range(len(data)):
                pass
                #print(data[i][2])
                #data[i][2] = filename.strip("./")
            print(data)


generate()