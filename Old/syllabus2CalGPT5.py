import csv
from datetime import datetime, timedelta

# Map weekday letters to offsets from Week Beginning
DAY_OFFSETS = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4}

INPUT_FILE = "input.csv"
OUTPUT_FILE = "google_calendar.csv"


def parse_events():
    events = []

    with open(INPUT_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            week_start_str = row["Week\nBeginning"].strip()
            if not week_start_str:
                continue

            # Parse the week start date
            try:
                week_start = datetime.strptime(week_start_str, "%m/%d/%y")
            except ValueError:
                try:
                    week_start = datetime.strptime(week_start_str, "%m/%d/%Y")
                except ValueError:
                    continue  # Skip bad dates

            # Split Topic/Activity and Readings by lines
            topics = row['\nTopic/Activity'].splitlines()
            readings = row['\nReadings'].splitlines()

            # Process both topics and readings
            for entry_list, prefix in [(topics, "Topic/Activity"), (readings, "Reading")]:
                for entry in entry_list:
                    entry = entry.strip()
                    if not entry:
                        continue

                    # Expect format like "M: Some text"
                    if len(entry) > 1 and entry[1] == ":":
                        day_letter = entry[0].upper()
                        text = entry[2:].strip()
                    else:
                        # If not prefixed, skip or assign to Monday
                        day_letter = 'M'
                        text = entry

                    if not text or day_letter not in DAY_OFFSETS:
                        continue

                    event_date = week_start + timedelta(days=DAY_OFFSETS[day_letter])
                    events.append({
                        "Subject": text,
                        "Start Date": event_date.strftime("%m/%d/%Y"),
                        "All Day Event": "True",
                        "Description": prefix
                    })

    return events


def write_google_calendar_csv(events):
    fieldnames = ["Subject", "Start Date", "All Day Event", "Description"]
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for event in events:
            writer.writerow(event)


if __name__ == "__main__":
    events = parse_events()
    write_google_calendar_csv(events)
    print(f"Done! Wrote {len(events)} events to {OUTPUT_FILE}")
