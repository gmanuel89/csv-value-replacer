# Create a dictionary of "old"-"new" value couples from a CSV file content
def create_replacing_map(input_csv_lines):
    # Get header
    csv_header = input_csv_lines[0]
    # Remove it from the list
    input_csv_lines.remove(csv_header)
    # Determine the indices of the "new" and the "old"
    new_index = None
    old_index = None
    column_index = None
    for i in range(len(csv_header)):
        if 'old' in csv_header[i].lower():
            old_index = i
    for i in range(len(csv_header)):
        if 'new' in csv_header[i].lower():
            new_index = i
    for i in range(len(csv_header)):
        if 'column' in csv_header[i].lower():
            column_index = i
    # Build the list of dictionaries
    mapping_dictionary_array = []
    # If the "column" is not specified
    if new_index is not None and old_index is not None and column_index is None:
        for i in range(len(input_csv_lines)):
            mapping_dictionary = {'old' : input_csv_lines[i][old_index], 'new' : input_csv_lines[i][new_index]}
            mapping_dictionary_array.append(mapping_dictionary)
    # If the "column" is specified
    elif new_index is not None and old_index is not None and column_index is not None:
        for i in range(len(input_csv_lines)):
            # retrieve the individual column names (stripped from spaces)
            column_indices = input_csv_lines[i][column_index].split(',')
            for c in range(len(column_indices)):
                column_indices[c] = column_indices[c].strip()
            mapping_dictionary = {'old' : input_csv_lines[i][old_index], 'new' : input_csv_lines[i][new_index], 'columns' : column_indices}
            mapping_dictionary_array.append(mapping_dictionary)
    # Return
    print(mapping_dictionary_array)
    return mapping_dictionary_array