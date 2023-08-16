"""
Script: Email Address Finder
Version: 1.0
Author: Jack Atherton
Synopsis: This script searches for valid email addresses in a text file and prints the matching lines.

Description:
This script reads a text file specified by the user and searches for lines containing valid email addresses.
It uses a regular expression pattern to identify email addresses, and it prints the line numbers and the
entire lines where matches are found.
"""

import re

def is_valid_email(address):
    # Regular expression pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.search(email_pattern, address)

def find_email_addresses_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_valid_email(line):
                    print(f"Line {line_number}: {line.strip()}")  # Print line number and the entire line
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = input('Please enter the filename to search: ')
    find_email_addresses_in_file(file_path)
