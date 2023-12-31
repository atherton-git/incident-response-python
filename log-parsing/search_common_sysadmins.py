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

import os
import re

COMMON_USERNAMES = [
    'admin', 'root', 'administrator', 'sysadmin', 'superuser',
    'ubnt', 'operator', 'manager', 'supervisor', 'tech'
]

def is_common_username(username):
    return any(name in username.lower() for name in COMMON_USERNAMES)

def find_common_usernames_in_file(file_path):
    try:
        found_match = False  # Flag to track if any matches are found
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_common_username(line):
                    highlighted_line = re.sub(
                        fr'\b({"|".join(map(re.escape, COMMON_USERNAMES))})\b', 
                        r"\033[32m\1\033[0m", 
                        line, 
                        flags=re.IGNORECASE
                    )
                    print(f"Line {line_number}: {highlighted_line}", end='')  # Print the modified line
                    found_match = True
            if not found_match:
                print("\033[31mNo matches found, or EOF.\033[0m")  # Print in red
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def find_common_usernames_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning file: {file_path}")
            find_common_usernames_in_file(file_path)
            print("-" * 40)

if __name__ == "__main__":
    path = input('Please enter the filename or directory to search: ')
    
    if os.path.isfile(path):
        find_common_usernames_in_file(path)
    elif os.path.isdir(path):
        find_common_usernames_in_directory(path)
    else:
        print(f"Path not found: {path}")
