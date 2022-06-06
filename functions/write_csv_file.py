## Import libraries
import csv


## Write CSV content into a file
def write_csv_file(csv_file_content, output_file_name):
    # Check output file name
    if output_file_name == '' : output_file_name = 'CSV file'
    if not output_file_name.endswith('.csv') : output_file_name = output_file_name + '.csv'
    # Write file content
    with open (output_file_name, 'w+', encoding='UTF8', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        # If it is a list of row...
        if isinstance(csv_file_content, list):
            for line in csv_file_content:
                csv_writer.writerow(line)
        else:
            import openpyxl
            if isinstance(csv_file_content, openpyxl.worksheet.worksheet.Worksheet):
                for row in csv_file_content.rows:
                    excel_output_row = []
                    for c in row:
                        excel_output_row.append(c.value)
                    csv_writer.writerow(excel_output_row)
            else:
                pass
    # Close the file
    output_file.close()