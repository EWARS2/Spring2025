import csv
from datetime import datetime, timedelta

# Input and output CSV file names
INPUT_FILE = "input.csv"
OUTPUT_FILE = "google_calendar.csv"

# Google Calendar CSV headers
GCAL_HEADERS = [
    "Subject", "Start Date", "Start Time", "End Date", "End Time",
    "All Day Event", "Description", "Location", "Private"
]

# Weekday offsets: Monday = 0, Tuesday = 1, ..., Friday = 4
WEEKDAY_OFFSETS = [0, 1, 2, 3, 4]

def parse_multiline_cell(cell):
    """
    Split a cell by line breaks, strip whitespace, and filter out empty lines.
    """
    lines = [line.strip() for line in cell.splitlines() if line.strip()]
    return lines

def create_event(subject, date):
    """
    Create a Google Calendar event row (all-day event).
    """
    return {
        "Subject": subject,
        "Start Date": date.strftime("%m/%d/%Y"),
        "Start Time": "",
        "End Date": date.strftime("%m/%d/%Y"),
        "End Time": "",
        "All Day Event": "True",
        "Description": "",
        "Location": "",
        "Private": "True"
    }

def convert_csv():
    events = []

    with open(INPUT_FILE, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            week_start_str = row["Week Beginning"].strip()
            if not week_start_str:
                continue  # Skip rows with no week start

            week_start = datetime.strptime(week_start_str, "%m/%d/%y")

            topics = parse_multiline_cell(row["Topic/Activity"])
            readings = parse_multiline_cell(row["Readings"])

            # Ensure both lists have length <= 5 (M-F); fill shorter lists with blanks
            for i, topic in enumerate(topics):
                if topic:
                    date = week_start + timedelta(days=WEEKDAY_OFFSETS[i])
                    events.append(create_event(f"Topic: {topic}", date))

            for i, reading in enumerate(readings):
                if reading:
                    date = week_start + timedelta(days=WEEKDAY_OFFSETS[i])
                    events.append(create_event(f"Reading: {reading}", date))

    # Write output CSV
    with open(OUTPUT_FILE, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=GCAL_HEADERS)
        writer.writeheader()
        for event in events:
            writer.writerow(event)

    print(f"Conversion complete! {len(events)} events written to {OUTPUT_FILE}")

if __name__ == "__main__":
    convert_csv()
