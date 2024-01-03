import csv

def read_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
    return data

def write_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")

def find_min_max_in_row(row):
    values = [float(value) for value in row.values() if value.replace('.', '', 1).isdigit()]
    if not values:
        return None, None
    return min(values), max(values)

def main():
    input_filename = 'Ukraine.csv'
    output_filename = 'Ukraine1.csv'

    data = read_csv(input_filename)

    for row in data:
        print(row)

    headers = data[0].keys()
    print(f"\nAll Column Names: {headers}")

    row_index = 0

    min_value, max_value = find_min_max_in_row(data[row_index])
    print(f"\nMinimum value in the row: {min_value}")
    print(f"Maximum value in the row: {max_value}")

    output_data = [{'Min Inflation': min_value, 'Max Inflation': max_value}]
    write_csv(output_filename, output_data)

if __name__ == "__main__":
    main()
