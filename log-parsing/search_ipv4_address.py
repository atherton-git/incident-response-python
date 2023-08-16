"""
Script: IPv4 Address Finder
Version: 1.0
Author: Jack Atherton
Synopsis: This script searches for valid IPv4 addresses in a text file and prints the matching lines.

Description:
This script reads a text file specified by the user and searches for lines containing valid IPv4 addresses.
It uses a regular expression pattern to identify IPv4 addresses, and it prints the line numbers and the
entire lines where matches are found.
"""

import re

def is_valid_ip(address):
    # Regular expression pattern to match IPv4 addresses
    ip_pattern = r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)"
    return re.search(ip_pattern, address)

def find_ip_addresses_in_file(file_path):
    try:
        found_match = False  # Flag to track if any matches are found
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_valid_ip(line):
                    print(f"\033[34mLine {line_number}: {line.strip()}\033[0m")  # Print in blue
                    found_match = True
            if not found_match:
                print("\033[31mNo matches found.\033[0m")  # Print "No matches found" in red
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = input('Please enter the filename to search: ')
    find_ip_addresses_in_file(file_path)
