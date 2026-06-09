import csv
from datetime import datetime, timedelta

NAME = "Sustainability"
SUBJECT_COLUMN = 2
DATE_COLUMN = 0

INPUT = NAME + ".csv"
OUTPUT = NAME + "Due_Cal.csv"
DATE_APPEND = " 2025"
DATE_TRIM = 2

global output
output = "Subject,Start Date"
formats = ["%m/%d/%y", "%B %d %Y", "%m/%d/%y %I:%M %p", "%b %d %Y"]

def create_date(subject, start_date):
    if (subject in [None, ""]) or (start_date in [None, ""]):
        return
    global output
    subject = subject.strip()
    start_date = start_date.strftime(formats[0])
    output+=("\n\"" + subject + "\"," + start_date)

def convert_date(new_date):
    new_date += DATE_APPEND
    new_date = new_date[DATE_TRIM:len(new_date)]
    for i in formats:
        try:
            new_date = datetime.strptime(new_date, i)
            return new_date
        except:
            continue
    return None

with open(INPUT, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)


for rows in data:
    date = rows[DATE_COLUMN].strip()
    date = convert_date(date)
    row = rows[SUBJECT_COLUMN].split('\n')
    for i in row:
        create_date(i, date)

print(output)

with open(OUTPUT, 'w') as file:
    file.write(output)
