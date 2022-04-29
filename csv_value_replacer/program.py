# Import libraries
from csv_value_replacer.libraries import *
from parameters import *
from csv_value_replacer.create_replacing_map import create_replacing_map
from csv_value_replacer.replace_csv_values import replace_csv_values

from tkinter import *
from tkinter import Entry, messagebox, filedialog
import csv

# Input CSV file (to be replaced)
Tk().withdraw()
input_csv_file = filedialog.askopenfilename(filetypes=[('CSV files', '.csv')])
Tk().withdraw()
messagebox.showinfo(title='CSV file selected', message="The CSV file selected is '%s'" % (input_csv_file))
# Read the input CSV
with open(input_csv_file, 'r', encoding='UTF8') as input_file:
    # Read CSV file lines
    input_csv_file_lines = list(csv.reader(input_file))

# Input CSV file (with replacing map --> "Old value" ; "New value")
Tk().withdraw()
input_csv_file_with_map = filedialog.askopenfilename(filetypes=[('CSV files', '.csv')])
Tk().withdraw()
messagebox.showinfo(title='CSV file selected', message="The CSV file selected is '%s'" % (input_csv_file_with_map))
# Open CSV with mapping
with open(input_csv_file_with_map, 'r', encoding='UTF8') as input_file:
    input_csv_file_with_map_lines = list(csv.reader(input_file))

# Create the map
mapping_dictionary_array = create_replacing_map(input_csv_file_with_map_lines)

# Generate the output
output_csv_file_lines = replace_csv_values(input_csv_file_lines, mapping_dictionary_array)

# Write the output file onto the input file   
with open (input_csv_file, 'w+', encoding='UTF8', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    for line in output_csv_file_lines:
            csv_writer.writerow(line)
