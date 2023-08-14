import re

def contains_http_url(line):
    # Regular expression pattern to match http:// or https://
    url_pattern = r"(http://|https://)\S+|:\d+$"
    return re.search(url_pattern, line)

def find_http_urls_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if contains_http_url(line):
                    print(f"Line {line_number}: {line.strip()}")  # Print line number and the entire line
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Define the path of the file you wish to parse
find_http_urls_in_file(input('Please enter the filename to search: '))
