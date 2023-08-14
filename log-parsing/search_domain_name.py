import re
import requests

def download_tld_list(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.split()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading TLD list: {e}")
        return []

def is_valid_string(s, tld_list):
    # Regular expression pattern to match URLs with any valid TLD from the provided list
    tld_pattern = "|".join(tld_list)
    string_pattern = r'\b(?:https?://)?[A-Za-z0-9.-]+\.(?:' + tld_pattern + r')\b'
    return re.search(string_pattern, s)

def find_strings_in_file(file_path, tld_list):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if is_valid_string(line, tld_list):
                    print(f"Line {line_number}: {line.strip()}")  # Print line number and the entire line
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Define the URL to download the TLD list
tld_url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
tld_list = download_tld_list(tld_url)

# Define the path of the file you wish to parse
find_strings_in_file(input('Please enter the filename to search: '), tld_list)
