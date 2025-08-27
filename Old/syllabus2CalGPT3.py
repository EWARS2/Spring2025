import csv
from datetime import datetime, timedelta

# Map weekdays to offsets
WEEKDAY_MAP = {
    'M': 0,
    'T': 1,
    'W': 2,
    'R': 3,
    'F': 4
}

# Google Calendar CSV headers
GCAL_HEADERS = [
    "Subject", "Start Date", "Start Time", "End Date", "End Time",
    "All Day Event", "Description", "Location", "Private"
]


def parse_lines(cell):
    """Split multi-line cell content into non-empty stripped lines."""
    return [line.strip() for line in cell.splitlines() if line.strip()]


def convert_to_gcal(input_csv, output_csv):
    with open(input_csv, newline='', encoding='utf-8') as infile, \
            open(output_csv, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(GCAL_HEADERS)

        for row in reader:
            week_start_str = row.get("Week\nBeginning", "").strip()
            if not week_start_str:
                continue

            # Parse week start date
            try:
                week_start = datetime.strptime(week_start_str, "%m/%d/%y")
            except ValueError:
                continue

            topics = parse_lines(row.get("Topic/Activity", ""))
            readings = parse_lines(row.get("Readings", ""))

            # Process topics
            for topic in topics:
                if ": " in topic:
                    day_letter, event = topic.split(": ", 1)
                    day_letter = day_letter.strip()
                    event = event.strip()
                    if event:
                        event_date = week_start + timedelta(days=WEEKDAY_MAP.get(day_letter, 0))
                        writer.writerow([event, event_date.strftime("%m/%d/%Y"), "",
                                         event_date.strftime("%m/%d/%Y"), "", "True", "", "", "True"])

            # Process readings (assume first reading is for Wednesday, second for Friday, etc.)
            for idx, reading in enumerate(readings):
                # If fewer than 5 readings, place them on Wed/Fri as per your example
                weekday_offset = [2, 4][idx % 2] if len(readings) <= 2 else idx
                event_date = week_start + timedelta(days=weekday_offset)
                writer.writerow([reading, event_date.strftime("%m/%d/%Y"), "",
                                 event_date.strftime("%m/%d/%Y"), "", "True", "", "", "True"])

# Example usage:
convert_to_gcal("input.csv", "google_calendar.csv")
