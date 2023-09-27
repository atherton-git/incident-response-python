import os
import re
import pandas as pd
from datetime import datetime

# User-defined variables
log_directory = r"/tmp/logfiles/"
output_file = r'/tmp/output.csv'

def process_log_entry(timestamp_string, line, line_number, current_year, relative_path, channel):
    # Check if the log payload has been processed before
    if line.strip() not in processed_payloads:
        timestamp = None
        formats_to_try = [('%Y %b %d %H:%M:%S', f"{current_year} {timestamp_string}"),  # Example: '1900 Jan 01 12:00:00'
                          ('%Y %b %d %H:%M:%S.%f', f"{current_year} {timestamp_string}"),  # Example: '1900 Jan 01 12:00:00.000000'
                          ('%Y-%m-%d %H:%M:%S', timestamp_string),  # Example: '1900-01-01 12:00:00'
                          ('%d/%b/%Y:%H:%M:%S', timestamp_string)]  # Example: '01/Jan/1900:12:00:00'
        
        for format_to_try, formatted_timestamp_string in formats_to_try:
            try:
                timestamp = datetime.strptime(formatted_timestamp_string, format_to_try)
                break  # Stop trying if one format succeeds
            except ValueError:
                pass

        if timestamp:
            timestamps.append({'Time Generated': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                               'Filename': relative_path,
                               'Line': line_number,
                               'Channel': channel,
                               'Payload': line.strip()})
            processed_payloads.add(line.strip())
            print(f"Processed timestamp {timestamp.strftime('%Y-%m-%d %H:%M:%S')} in file {relative_path} (Line {line_number})")

current_year = datetime.now().year
timestamps = []
processed_payloads = set()

patterns = [r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2})',  # Example: 'Jan 01 12:00:00'
            r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}\.\d{6})',  # Example: 'Jan 01 12:00:00.000000'
            r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',  # Example: '1900-01-01 12:00:00'
            r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})']  # Example: '01/Jan/1900:12:00:00'

print(f"Searching for log files in {log_directory} and its subdirectories...")

for root, _, files in os.walk(log_directory):
    for file in files:
        current_file = os.path.join(root, file)
        relative_path = os.path.relpath(current_file, log_directory)
        channel = channel = os.path.splitext(file)[0].split('.')[0]

        try:
            with open(current_file, 'r', encoding='unicode_escape') as reader:
                line_number = 1

                for line in reader:
                    for pattern in patterns:
                        matches = re.finditer(pattern, line)
                        for match in matches:
                            timestamp_string = match.group(1)
                            process_log_entry(timestamp_string, line, line_number, current_year, relative_path, channel)

                    line_number += 1
        except Exception as e:
            print(f"Error processing file {relative_path}: {str(e)}")

df = pd.DataFrame(timestamps)
df.to_csv(output_file, index=False)
print(f"Processing completed. Total timestamps processed: {len(timestamps)}")
