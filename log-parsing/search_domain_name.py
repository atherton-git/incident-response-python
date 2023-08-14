import re

def is_valid_domain(domain):
    # Regular expression pattern to match domain names
    domain_pattern = r"([\w+]+\:\/\/)?([\w\d-]+\.)*[\w-]+[\.\:]\w+([\/\?\=\&\#\.]?[\w-]+)*\/?"
    return re.search(domain_pattern, domain)

def find_domains_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                domains = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', line)
                for domain in domains:
                    if is_valid_domain(domain):
                        print(f"Line {line_number}: {domain}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Define the path of the file you wish to parse
find_domains_in_file(input('Please enter the filename to search: '))
