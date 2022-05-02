# Import libraries
from csv_value_replacer.libraries import *
from csv_value_replacer.create_replacing_map import create_replacing_map
from csv_value_replacer.replace_csv_values import replace_csv_values


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
    with open(input_csv_file_with_map, 'r', encoding='UTF8') as input_file:
        input_csv_file_with_map_lines = list(csv.reader(input_file))
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
    with open(input_csv_file, 'r', encoding='UTF8') as input_file:
        # Read CSV file lines
        input_csv_file_lines = list(csv.reader(input_file))
    # Generate the output
    output_csv_file_lines = replace_csv_values(input_csv_file_lines, mapping_dictionary_array)
    # Write the output file onto the input file   
    with open (input_csv_file, 'w+', encoding='UTF8', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        for line in output_csv_file_lines:
                csv_writer.writerow(line)
    # Success
    Tk().withdraw()
    messagebox.showinfo(title='Success', message="The selected the CSV file:\n'%s'\nwas successfully processed" % (input_csv_file))