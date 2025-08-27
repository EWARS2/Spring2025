import csv
from datetime import datetime, timedelta

INPUT = "input.csv"
OUTPUT = "google_calendar.csv"

global output
output = "Subject,Start Date"
format = "%m/%d/%y"


def create_date(Subject,Start_Date):
    global output
    Subject = Subject.strip()
    Start_Date = Start_Date.strftime(format)
    if (Subject != ""):
        output+=("\n\""+Subject+"\","+Start_Date)

with open(INPUT, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)


for rows in data:
    start_date = rows[0].strip()
    start_date = datetime.strptime(start_date, format)
    row = rows[1].split('\n')
    for i in row:
        create_date(i,start_date)
        start_date = start_date + timedelta(days=1)

    start_date = rows[0].strip()
    start_date = datetime.strptime(start_date, format)
    row = rows[2].split('\n')
    for i in row:
        create_date(i, start_date)
        start_date = start_date + timedelta(days=1)


with open(OUTPUT, 'w') as file:
    file.write(output)