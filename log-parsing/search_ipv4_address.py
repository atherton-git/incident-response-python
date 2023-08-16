import re

def is_valid_ip(address):
    # Regular expression pattern to match IPv4 addresses
    ip_pattern = r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)"
    return re.search(ip_pattern, address)

def find_ip_addresses_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_valid_ip(line):
                    print(f"Line {line_number}: {line.strip()}")  # Print line number and the entire line
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Define the path of the file you wish to parse
find_ip_addresses_in_file(input('Please enter the filename to search: '))
