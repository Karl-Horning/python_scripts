# Python Scripts Repository

Welcome to my Python Scripts repository! This repository contains various Python scripts for different tasks and projects.

## Scripts

### 1. api/scrape_wikipedia_pages.py

This script scrapes Wikipedia pages to extract information about category members and saves them to a CSV file.

#### Usage

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/Karl-Horning/python_scripts.git
   ```

2. Navigate to the Python Scripts directory:
   ```
   cd python_scripts/api
   ```

3. Run the script using python3:
   ```
   python3 scrape_wikipedia_pages.py
   ```

#### Dependencies

- Python 3.x
- requests library (install via pip3 if not already installed)
- csv library (built-in)
- re library (built-in)

#### Output

The script will create a CSV file named "given_names.csv" in the same directory where the script is located. This file contains the extracted information about category members from Wikipedia.

### 2. pandas/compare_excel_sheets.py

This script compares multiple sheets in an Excel workbook and highlights the differences.

#### Usage

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/Karl-Horning/python_scripts.git
   ```

2. Navigate to the Python Scripts directory:
   ```
   cd python_scripts/pandas
   ```

3. Run the script:
   ```
   python3 compare_excel_sheets.py
   ```

#### Dependencies

- Python 3.x
- pandas library (install via pip3 if not already installed)
- openpyxl library (install via pip3 if not already installed)

#### Description

The script reads the specified Excel workbook and compares the specified sheets. It then highlights the differences between the sheets and saves the results to a new Excel file.

#### Input

- `input_file`: Path to the input Excel workbook.
- `sheet_names`: List of sheet names to compare.
- `output_file`: Path to the output Excel file to save the differences.

## Contribution

Feel free to contribute to this repository by adding more scripts or improving existing ones. You can fork the repository, make your changes, and submit a pull request.

Happy coding!

## Author

Karl Horning: [GitHub](https://github.com/Karl-Horning/) | [LinkedIn](https://www.linkedin.com/in/karl-horning/) | [CodePen](https://codepen.io/karlhorning)
