# Create a dictionary of "old"-"new" value couples from a CSV file content
def create_replacing_map(input_csv_lines):
    # Get header
    csv_header = input_csv_lines[0]
    # Remove it from the list
    input_csv_lines.remove(csv_header)
    # Determine the indices of the "new" and the "old"
    new_index = None
    old_index = None
    for i in range(len(csv_header)):
        if 'old' in csv_header[i].lower():
            old_index = i
    for i in range(len(csv_header)):
        if 'new' in csv_header[i].lower():
            new_index = i
    # Build the list of dictionaries
    mapping_dictionary_array = []
    if new_index is not None and old_index is not None:
        for i in range(len(input_csv_lines)):
            mapping_dictionary = {'old' : input_csv_lines[i][old_index], 'new' : input_csv_lines[i][new_index]}
            mapping_dictionary_array.append(mapping_dictionary)
    # Return
    return mapping_dictionary_array