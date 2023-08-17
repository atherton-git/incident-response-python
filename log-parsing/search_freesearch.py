import os

def find_text_in_file(file_path, search_query):
    try:
        if os.path.isdir(file_path):
            for root, _, files in os.walk(file_path):
                for file_name in files:
                    file_to_search = os.path.join(root, file_name)
                    search_in_single_file(file_to_search, search_query)
        elif os.path.isfile(file_path):
            search_in_single_file(file_path, search_query)
        else:
            print("Invalid path provided.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_in_single_file(file_path, search_query):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if search_query in line:
                    highlighted_line = line.replace(search_query, f"\033[32m{search_query}\033[0m")
                    print(f"File: {file_path}, Line {line_number}: {highlighted_line.strip()}")
            if not any(search_query in line for line in file):
                print(f"File: {file_path}, No matches found, or EOF.")  # Print file path and message
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

if __name__ == "__main__":
    path = input('Please enter the file or directory path to search: ')
    search_query = input('Please enter the search query: ')
    find_text_in_file(path, search_query)
