## Import libraries
import csv
import sys

## Read input csv file (returns a list of rows)
def read_csv_file(input_csv_file):
    # Open the CSV file and convert it to a list
    with open (input_csv_file, 'r', encoding='UTF8', newline='') as input_file:
        # Prevent possible errors due to large columns (beyond 131072 characters)
        try:
            input_csv_file_lines = list(csv.reader(input_file))
        except:
            print("Presence of too large cells!!!")
            field_size_limit = sys.maxsize
            while True:
                try:
                    csv.field_size_limit(field_size_limit)
                    break
                except:
                    field_size_limit = int(field_size_limit / 10)
            input_csv_file_lines = list(csv.reader(input_file))
    # return
    return input_csv_file_lines