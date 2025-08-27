import csv
import datetime

# Map weekday letters to Python weekday offsets
WEEKDAY_MAP = {
    'M': 0,  # Monday
    'T': 1,  # Tuesday
    'W': 2,  # Wednesday
    'R': 3,  # Thursday
    'F': 4   # Friday
}

INPUT_FILE = "input.csv"
OUTPUT_FILE = "google_calendar.csv"

def parse_week_start(date_str):
    """Parse Week Beginning date into a datetime.date."""
    return datetime.datetime.strptime(date_str.strip(), "%m/%d/%y").date()

def create_event(subject, date, description=""):
    """Create a Google Calendar row."""
    return {
        "Subject": subject.strip(),
        "Start Date": date.strftime("%m/%d/%Y"),
        "Start Time": "",
        "End Date": date.strftime("%m/%d/%Y"),
        "End Time": "",
        "All Day Event": "True",
        "Description": description.strip()
    }

def main():
    events = []
    with open(INPUT_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            week_start = parse_week_start(row["Week\nBeginning"])
            topics = row["\nTopic/Activity"].splitlines()
            readings = row["\nReadings"].splitlines()

            # Clean empty lines
            topics = [t for t in topics if t.strip()]
            readings = [r for r in readings if r.strip()]

            # Match weekdays in Topics
            for topic in topics:
                day_letter = topic.strip()[0]
                if day_letter in WEEKDAY_MAP:
                    date = week_start + datetime.timedelta(days=WEEKDAY_MAP[day_letter])
                    subject = topic[2:].strip()  # remove "X: "
                    events.append(create_event(subject, date))

            # Create reading events separately (on Monday by default)
            for r in readings:
                # Place readings on Monday of that week
                date = week_start
                events.append(create_event(f"Reading: {r}", date))

    # Write Google Calendar CSV
    fieldnames = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description"]
    with open(OUTPUT_FILE, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for e in events:
            writer.writerow(e)

    print(f"✅ Converted CSV saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
