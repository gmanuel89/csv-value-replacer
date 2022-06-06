# Replace the csv values according to a list of dictionaries with 'old' and 'new' values
def replace_csv_values(input_csv_file_lines, mapping_dictionary_array):
    # Run if there is a map (otherwise return the input file with no modifications)
    if len(mapping_dictionary_array) == 0: return input_csv_file_lines
    # See if there is a match with the mapping array
    for maprepl in mapping_dictionary_array:
        # If there is no column(s) specified, go for the all-cell replacement
        if maprepl.get('columns') is None:
            # For each row...
            for r in range(len(input_csv_file_lines)):
                # Skip the header
                if r == 0 : continue
                # For each column
                for c in range(len(input_csv_file_lines[r])):     
                    # Replace the cell value
                    if str(input_csv_file_lines[r][c]) == str(maprepl.get('old')):
                        input_csv_file_lines[r][c] = str(maprepl.get('new'))
        else:
            # Determine the indices of the columns (compare mapping with the header)
            columns = maprepl.get('columns')
            column_indices = []
            for i in range(len(columns)):
                for c in range(len(input_csv_file_lines[0])):
                    if columns[i] == input_csv_file_lines[0][c]:
                        column_indices.append(c)
            # Replace all the values only in selected columns
            # For each row...
            for r in range(len(input_csv_file_lines)):
                # Skip the header
                if r == 0 : continue
                # For each column
                if len(column_indices) == 0:
                    for c in range(len(input_csv_file_lines[r])):     
                        # Replace the cell value
                        if str(input_csv_file_lines[r][c]) == str(maprepl.get('old')):
                            input_csv_file_lines[r][c] = str(maprepl.get('new'))
                else:
                    # For each column (to replace)
                    for c in column_indices:     
                        # Replace the cell value
                        if str(input_csv_file_lines[r][c]) == str(maprepl.get('old')):
                            input_csv_file_lines[r][c] = str(maprepl.get('new'))  
    # Return
    return input_csv_file_lines