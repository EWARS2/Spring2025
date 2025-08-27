# It's almost bloody midight Im falling askeeep don;t judge
# lpeas just workmn
import csv
from datetime import datetime, timedelta

INPUT_FILE = "input.csv"
OUTPUT_FILE = "google_calendar.csv"

# Weekday names for mapping (assuming 5 days: Monday-Friday)
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def parse_multiline_cell(cell):
    """Split multiline cell into list of lines, strip whitespace."""
    if not cell:
        return [""] * 5
    lines = [line.strip() for line in cell.split("\n")]
    # Ensure exactly 5 entries, pad or trim as needed
    lines = [l for l in lines if l != ""]  # Remove empty lines
    while len(lines) < 5:
        lines.append("")
    return lines[:5]


def main():
    events = []

    with open(INPUT_FILE, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            week_start = datetime.strptime(row["Week Beginning"], "%m/%d/%y")

            # Get topic and readings split into daily entries
            topics = parse_multiline_cell(row["Topic/Activity"])
            readings = parse_multiline_cell(row["Readings"])

            for i in range(5):  # Monday-Friday
                day_date = week_start + timedelta(days=i)

                # Create Topic event if not blank
                if topics[i]:
                    events.append({
                        "Subject": topics[i],
                        "Start Date": day_date.strftime("%m/%d/%Y"),
                        "All Day Event": "True",
                        "Description": "Topic/Activity"
                    })

                # Create Reading event if not blank
                if readings[i]:
                    events.append({
                        "Subject": readings[i],
                        "Start Date": day_date.strftime("%m/%d/%Y"),
                        "All Day Event": "True",
                        "Description": "Reading"
                    })

    # Write output CSV in Google Calendar format
    fieldnames = ["Subject", "Start Date", "All Day Event", "Description"]
    with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"Exported {len(events)} events to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
