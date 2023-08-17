"""
Script: Common Protocol Finder
Version: 1.0
Author: Jack Atherton
Synopsis: This script searches for HTTP URLs in a text file and prints the matching lines.

Description:
This script reads a text file specified by the user and searches for lines containing HTTP URLs.
It performs a pattern matching to identify URLs starting with http://, https://, ftp://, and other schemes,
and it prints the line numbers and the entire lines where matches are found.
"""

import re
import os

def contains_http_url(line):
    # Regular expression pattern to match various URL schemes
    url_pattern = r"(http://|https://|ftp://|sftp://|ssh://|smtp://|pop3://|imap://|telnet://|rdp://|vnc://|nfs://|ldap://)\S+"
    match = re.search(url_pattern, line)
    if match:
        return match.group()  # Return the exact matched URL
    return None

def find_http_urls_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                matched_url = contains_http_url(line)
                if matched_url:
                    highlighted_line = line.replace(matched_url, f"\033[32m{matched_url}\033[0m")
                    print(f"File: {file_path}, Line {line_number}: {highlighted_line.strip()}")
            if not any(contains_http_url(line) for line in file):
                print("\033[31m" + f"File: {file_path}, No matches found, or EOF." + "\033[0m")  # Print file path and message in red
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def find_http_urls_in_directory(directory_path):
    try:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_to_search = os.path.join(root, file_name)
                find_http_urls_in_file(file_to_search)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input('Please enter the file or directory path to search: ')
    
    if os.path.isdir(path):
        find_http_urls_in_directory(path)
    elif os.path.isfile(path):
        find_http_urls_in_file(path)
    else:
        print("Invalid path provided.")
