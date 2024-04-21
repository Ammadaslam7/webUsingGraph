import os
import csv

# Function to read the content of a .txt file
def read_txt_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content.strip()

# Function to iterate over files in a folder, read their content, and write to CSV
def create_csv_from_folder(folder_path, output_file):
    # Open the CSV file in write mode
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Define the headers for the CSV file
        fieldnames = ['Content', 'Type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the headers to the CSV file
        writer.writeheader()

        # Iterate over files in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is a .txt file
            if filename.endswith('.txt'):
                # Read the content of the .txt file
                content = read_txt_content(os.path.join(folder_path, filename))
                # Write the content and type to the CSV file
                writer.writerow({'Content': content, 'Type': 'Marketing and Sales'})

# Specify the input folder containing the .txt files
input_folder = r"C:\BSCS6\webUsingGraph\preprocessing\Marketing and Sales"

# Specify the output CSV file
output_csv = 'MarketingandSales.csv'

# Call the function to create the CSV file from the folder
create_csv_from_folder(input_folder, output_csv)

print(f"CSV file '{output_csv}' created successfully.")
