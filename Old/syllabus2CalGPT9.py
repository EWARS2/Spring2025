import csv
from datetime import datetime, timedelta

# Input and output file paths
INPUT_FILE = "input.csv"
OUTPUT_FILE = "google_calendar.csv"

# Weekdays (Mon-Fri)
WEEKDAY_COUNT = 5


def process_csv():
    events = []

    with open(INPUT_FILE, newline='', encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            week_start_str = row["Week Beginning"].strip()
            topics_raw = row["Topic/Activity"].strip()
            readings_raw = row["Readings"].strip()

            if not week_start_str:
                continue

            # Parse week start date
            week_start = datetime.strptime(week_start_str, "%m/%d/%y")

            # Split topics and readings into lines, keeping order
            topics = [t.strip() for t in topics_raw.splitlines() if t.strip()]
            readings = [r.strip() for r in readings_raw.splitlines() if r.strip()]

            # Generate events for topics
            for i, topic in enumerate(topics):
                event_date = week_start + timedelta(days=i % WEEKDAY_COUNT)
                events.append({
                    "Subject": topic,
                    "Start Date": event_date.strftime("%m/%d/%Y"),
                    "End Date": event_date.strftime("%m/%d/%Y"),
                    "All Day Event": "True"
                })

            # Generate events for readings
            for i, reading in enumerate(readings):
                event_date = week_start + timedelta(days=i % WEEKDAY_COUNT)
                events.append({
                    "Subject": reading,
                    "Start Date": event_date.strftime("%m/%d/%Y"),
                    "End Date": event_date.strftime("%m/%d/%Y"),
                    "All Day Event": "True"
                })

    # Write Google Calendar CSV
    with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as outfile:
        fieldnames = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description",
                      "Location"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for e in events:
            writer.writerow({
                "Subject": e["Subject"],
                "Start Date": e["Start Date"],
                "Start Time": "",
                "End Date": e["End Date"],
                "End Time": "",
                "All Day Event": e["All Day Event"],
                "Description": "",
                "Location": ""
            })


if __name__ == "__main__":
    process_csv()
    print(f"Converted events written to {OUTPUT_FILE}")
