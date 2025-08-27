import csv
from datetime import datetime, timedelta

# Map day abbreviations to weekday offsets
day_offsets = {
    'M': 0,
    'T': 1,
    'W': 2,
    'R': 3,  # Thursday
    'F': 4
}

def parse_csv(input_file, output_file):
    events = []

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            week_start_str = row['Week\nBeginning'].strip()
            topic_str = row['\nTopic/Activity'].strip()
            readings_str = row['\nReadings'].strip()

            # Parse week start date
            try:
                week_start = datetime.strptime(week_start_str, "%m/%d/%y")
            except ValueError:
                # Skip rows that don't have valid dates
                continue

            # Process Topic/Activity by weekday
            topics = topic_str.splitlines()
            for topic in topics:
                topic = topic.strip()
                if not topic:
                    continue
                day_abbrev = topic.split(':')[0].strip()
                if day_abbrev in day_offsets:
                    date = week_start + timedelta(days=day_offsets[day_abbrev])
                    event_name = topic.split(':', 1)[1].strip() if ':' in topic else topic
                    if event_name:
                        events.append({
                            'Subject': event_name,
                            'Start Date': date.strftime("%m/%d/%Y"),
                            'All Day Event': 'True',
                            'Description': ''
                        })

            # Process readings as separate events
            readings = [r.strip() for r in readings_str.splitlines() if r.strip()]
            for reading in readings:
                events.append({
                    'Subject': reading,
                    'Start Date': week_start.strftime("%m/%d/%Y"),  # default to Monday of that week
                    'All Day Event': 'True',
                    'Description': 'Reading'
                })

    # Write output CSV in Google Calendar format
    fieldnames = ['Subject', 'Start Date', 'All Day Event', 'Description']
    with open(output_file, 'w', newline='', encoding='utf-8') as out_csv:
        writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"Converted calendar saved to {output_file}")

# Example usage
parse_csv('input.csv', 'google_calendar.csv')
