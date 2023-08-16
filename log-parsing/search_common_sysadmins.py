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
    return any(re.search(fr'\b{re.escape(name)}\b', username, re.IGNORECASE) for name in common_usernames)

def find_common_usernames_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                matches = []
                for match in re.finditer(fr'\b({"|".join(re.escape(name) for name in common_usernames)})\b', line, re.IGNORECASE):
                    matches.append(match.group())
                
                if matches:
                    highlighted_line = line
                    for match in matches:
                        highlighted_line = highlighted_line.replace(match, f"\033[32m{match}\033[0m")
                    print(f"Line {line_number}: {highlighted_line}", end='')  # Print with matches highlighted in green
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = input('Please enter the filename to search: ')
    find_common_usernames_in_file(file_path)
