import csv
from datetime import datetime, timedelta

# Map weekday abbreviations to weekday index
WEEKDAY_MAP = {
    'M': 0,  # Monday
    'T': 1,  # Tuesday
    'W': 2,  # Wednesday
    'R': 3,  # Thursday
    'F': 4,  # Friday
}

# Google Calendar header
GCAL_HEADER = [
    "Subject", "Start Date", "Start Time", "End Date", "End Time",
    "All Day Event", "Description", "Location"
]

def parse_weekday_entries(week_text):
    """
    Parse a block like:
    'M: No Class\nT: Course Intro\nW: Review Java'
    into a dict {weekday: event_text}
    """
    events = {}
    for line in week_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if ':' in line:
            day, text = line.split(':', 1)
            day = day.strip()
            text = text.strip()
            if day in WEEKDAY_MAP and text:
                events[day] = text
    return events

def main(input_csv, output_csv):
    rows_out = [GCAL_HEADER]

    with open(input_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            week_start_str = row["Week\nBeginning"].strip()
            topics = row["\nTopic/Activity"].strip()
            readings = row["\nReadings"].strip()

            # Parse week start date
            try:
                week_start = datetime.strptime(week_start_str, "%m/%d/%y")
            except ValueError:
                # If row is final exam or malformed, skip
                continue

            # Extract daily topics
            events = parse_weekday_entries(topics)

            # Create events
            for day, desc in events.items():
                event_date = week_start + timedelta(days=WEEKDAY_MAP[day])
                rows_out.append([
                    desc,                              # Subject
                    event_date.strftime("%m/%d/%Y"),   # Start Date
                    "",                                # Start Time
                    event_date.strftime("%m/%d/%Y"),   # End Date
                    "",                                # End Time
                    "True",                            # All Day Event
                    readings.replace("\n", "; "),      # Description
                    ""                                 # Location
                ])

    # Write output CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows_out)

    print(f"Converted calendar saved to {output_csv}")


if __name__ == "__main__":
    main("input.csv", "google_calendar.csv")
