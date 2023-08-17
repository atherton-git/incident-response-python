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

import os
import re

def is_valid_email(address):
    # Regular expression pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    match = re.search(email_pattern, address)
    if match:
        return match.group()  # Return the exact matched email address
    return None

def find_email_addresses_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                matched_email = is_valid_email(line)
                if matched_email:
                    highlighted_line = line.replace(matched_email, f"\033[32m{matched_email}\033[0m")
                    print(f"Line {line_number}: {highlighted_line.strip()}")
            if not any(is_valid_email(line) for line in file):
                print("\033[31mNo matches found, or EOF.\033[0m")  # Print in red
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def find_email_addresses_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning file: {file_path}")
            find_email_addresses_in_file(file_path)
            print("-" * 40)

if __name__ == "__main__":
    path = input('Please enter the filename or directory to search: ')
    
    if os.path.isfile(path):
        find_email_addresses_in_file(path)
    elif os.path.isdir(path):
        find_email_addresses_in_directory(path)
    else:
        print(f"Path not found: {path}")
