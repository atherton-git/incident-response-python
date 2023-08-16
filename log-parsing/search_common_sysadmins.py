"""
Script: Common Usernames Finder
Version: 1.0
Author: Jack Atherton
Synopsis: This script searches for common administrative accounts within a cleartext log and prints the matching lines.

Description:
This script reads a text file specified by the user and searches for lines containing common administrative usernames.
It performs a case-insensitive search to match the usernames, and it prints the line numbers and the entire
lines where matches are found.

Common usernames: admin, root, administrator, sysadmin, superuser,
                  ubnt, operator, manager, supervisor, tech
"""

import re

def is_common_username(username):
    common_usernames = [
        'admin', 'root', 'administrator', 'sysadmin', 'superuser',
        'ubnt', 'operator', 'manager', 'supervisor', 'tech'
    ]
    return username.strip().lower() in common_usernames

def find_common_usernames_in_file(file_path):
    try:
        found_match = False  # Flag to track if any matches are found
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_common_username(line):
                    print(f"\033[31mLine {line_number}: {line.strip()}\033[0m")  # Print in red
                    found_match = True
            if not found_match:
                print("\033[31mNo matches found.\033[0m")  # Print "No matches found" in red
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = input('Please enter the filename to search: ')
    find_common_usernames_in_file(file_path)
