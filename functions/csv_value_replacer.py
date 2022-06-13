# Import libraries
from functions.libraries import *
from functions.create_replacing_map import *
from functions.replace_csv_values import *
from functions.read_csv_file import *
from functions.write_csv_file import *
import sys


# Input map CSV file (with replacing map --> "Old value" ; "New value")
Tk().withdraw()
messagebox.showinfo(title='Select map CSV file', message='Select the CSV file with the "old"-"new" map for value replacement')
Tk().withdraw()
input_csv_file_with_map = filedialog.askopenfilename(filetypes=[('CSV files', '.csv')])
Tk().withdraw()
messagebox.showinfo(title='CSV file selected', message="The CSV file selected is '%s'" % (input_csv_file_with_map))
# Try to read map only if a file is selected
if input_csv_file_with_map != "":
    # Open CSV with mapping
    input_csv_file_with_map_lines = read_csv_file(input_csv_file_with_map)
    # Create the map
    mapping_dictionary_array = create_replacing_map(input_csv_file_with_map_lines)
else :
    input_csv_file_with_map_lines = []
    mapping_dictionary_array = []


# Input CSV file (to be replaced)
Tk().withdraw()
messagebox.showinfo(title='Select CSV file', message='Select the CSV file with values to be replaced')
Tk().withdraw()
input_csv_file = filedialog.askopenfilename(filetypes=[('CSV files', '.csv')])
Tk().withdraw()
messagebox.showinfo(title='CSV file selected', message="The CSV file selected is '%s'" % (input_csv_file))
# Run only if a file is selected
if input_csv_file_with_map != "":
    # Read the input CSV
    input_csv_file_lines = read_csv_file(input_csv_file)
    # Generate the output
    output_csv_file_lines = replace_csv_values(input_csv_file_lines, mapping_dictionary_array, add_new_column_if_match_is_missing=True)
    # Write the output file onto the input file   
    write_csv_file(output_csv_file_lines, input_csv_file)
    # Success
    Tk().withdraw()
    messagebox.showinfo(title='Success', message="The selected the CSV file:\n'%s'\nwas successfully processed" % (input_csv_file))