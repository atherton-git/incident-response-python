import re

def is_valid_domain(domain):
    # Regular expression pattern to match domains
    domain_pattern = r'^(https?://)?([a-zA-Z0-9.-]+)(:\d+)?$'
    return re.match(domain_pattern, domain)

def find_domains_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                domain_match = is_valid_domain(line.strip())
                if domain_match:
                    protocol = domain_match.group(1) or ''
                    domain = domain_match.group(2)
                    port = domain_match.group(3) or ''
                    print(f"Line {line_number}: {protocol}{domain}{port}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Define the path of the file you wish to parse
find_domains_in_file(input('Please enter the filename to search: '))
