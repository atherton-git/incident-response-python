def find_text_in_file(file_path, search_query):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if search_query in line:
                    highlighted_line = line.replace(search_query, f"\033[32m{search_query}\033[0m")
                    print(f"Line {line_number}: {highlighted_line.strip()}")
            if not any(search_query in line for line in file):
                print("\033[31mNo matches found, or EOF.\033[0m")  # Print in red
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = input('Please enter the filename to search: ')
    search_query = input('Please enter the search query: ')
    find_text_in_file(file_path, search_query)
