# Replace the csv values according to a list of dictionaries with 'old' and 'new' values
def replace_csv_values(input_csv_file_lines, mapping_dictionary_array):
    # Run if there is a map (otherwise return the input file with no modifications)
    if len(mapping_dictionary_array) == 0: return input_csv_file_lines
    # For each cell...
    for r in range(len(input_csv_file_lines)):
        for c in range(len(input_csv_file_lines[r])):
            # See if there is a match with the mapping array
            for map in mapping_dictionary_array:
                if str(input_csv_file_lines[r][c]) == str(map.get("old")):
                    input_csv_file_lines[r][c] = str(map.get("new"))
    # Return
    return input_csv_file_lines