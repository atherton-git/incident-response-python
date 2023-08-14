import re

def is_valid_email(address):
    # Regular expression pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]{1,64}+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.search(email_pattern, address)

def find_email_addresses_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_valid_email(line):
                    print(f"Line {line_number}: {line.strip()}")  # Print line number and the entire line
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Define the path of the file you wish to parse
find_email_addresses_in_file(input('Please enter the filename to search: '))
