import csv
from datetime import datetime, timedelta

INPUT = "Eng.csv"
OUTPUT = "EngGoogle.csv"

global output
output = "Subject,Start Date"
format = "%m/%d/%y"
format2 = "%B %d %Y"

def create_date(Subject,Start_Date):
    global output
    Subject = Subject.strip()
    Start_Date = Start_Date.strftime(format)
    if (Subject != ""):
        output+=("\n\""+Subject+"\","+Start_Date)

def convert_date(date):
    try:
        date = datetime.strptime(date, format)
    except:
        try:
            date = datetime.strptime(date + " 2025", format2)
        except:
            date = None
    return date

with open(INPUT, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)




for rows in data:
    start_date = rows[0].strip()
    start_date = convert_date(start_date)
    row = rows[1].split('\n')
    if (start_date != None):
        for i in row:
            create_date(i, start_date)

print(output)

with open(OUTPUT, 'w') as file:
    file.write(output)
