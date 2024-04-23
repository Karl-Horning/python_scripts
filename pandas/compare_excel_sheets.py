import pandas as pd

def compare_sheets(input_file, sheet_names, output_file):
    # Read the sheets into pandas DataFrames
    dfs = [pd.read_excel(input_file, sheet_name=sheet, engine='openpyxl') for sheet in sheet_names]

    # Find differences and highlight them
    diff = pd.DataFrame()
    for i in range(len(dfs) - 1):
        current_diff = dfs[i].compare(dfs[i + 1], align_axis=0)
        diff = diff.append(current_diff)

    # Create an Excel writer object for the output file
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Write the differences to a new sheet
        diff.to_excel(writer, sheet_name='Differences', index=False)

if __name__ == "__main__":
    # Replace 'your_file.xlsx' with the path to your Excel workbook
    input_file = '/full/path/to/directory/your_file.xlsx'
    
    # Replace ['Sheet1', 'Sheet2', 'Sheet3'] with the names of the sheets you want to compare
    sheet_names = ['Sheet1', 'Sheet2', 'Sheet3']
    
    # Replace 'output_file.xlsx' with the desired output file name
    output_file = '/full/path/to/directory/differences_file.xlsx'

    compare_sheets(input_file, sheet_names, output_file)
