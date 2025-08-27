import csv
from datetime import datetime, timedelta

# Map weekday abbreviations to offsets (0 = Monday)
day_offsets = {
    'M': 0,
    'T': 1,
    'W': 2,
    'R': 3,  # R for Thursday
    'F': 4
}

# Input and output files
INPUT_FILE = "input.csv"
OUTPUT_FILE = "google_calendar.csv"


def parse_multiline_cell(cell):
    """Split multiline cell content into lines and strip whitespace."""
    return [line.strip() for line in cell.splitlines() if line.strip()]


def create_event(date_str, title):
    """Return a dict representing a Google Calendar event."""
    # Google Calendar expects full year
    date_obj = datetime.strptime(date_str, "%m/%d/%y")
    formatted_date = date_obj.strftime("%m/%d/%Y")
    return {
        "Subject": title,
        "Start Date": formatted_date,
        "End Date": formatted_date,
        "All Day Event": "True"
    }


def main():
    events = []

    with open(INPUT_FILE, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            week_start = row["Week\nBeginning"].strip()
            if not week_start:
                continue

            try:
                week_date = datetime.strptime(week_start, "%m/%d/%y")
            except ValueError:
                continue  # Skip bad dates

            # Parse topics and readings
            topics = parse_multiline_cell(row.get("Topic/Activity", ""))
            readings = parse_multiline_cell(row.get("Readings", ""))

            # Process topics
            for entry in topics:
                if len(entry) > 1 and entry[1] == ':':
                    day_code = entry[0]
                    text = entry[2:].strip()
                else:
                    continue

                if day_code in day_offsets and text:
                    event_date = (week_date + timedelta(days=day_offsets[day_code])).strftime("%m/%d/%y")
                    events.append(create_event(event_date, text))

            # Process readings (assign sequentially to weekdays)
            for i, reading in enumerate(readings):
                if reading:
                    event_date = (week_date + timedelta(days=i)).strftime("%m/%d/%y")
                    events.append(create_event(event_date, f"Reading: {reading}"))

    # Write Google Calendar CSV
    fieldnames = ["Subject", "Start Date", "End Date", "All Day Event"]
    with open(OUTPUT_FILE, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"Converted {len(events)} events to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
