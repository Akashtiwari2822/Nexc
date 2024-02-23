import csv
import os


def create_csv(file_path, header):
    print("call the page")
    # Check if the file already exists
    directory = os.path.dirname(file_path)

    # Check if the directory exists; if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Check if the file already exists
    if not os.path.isfile(file_path):
        # If the file doesn't exist, create a new one with the specified header
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
        print(f"CSV file created at {file_path} with header: {','.join(header)}")
    else:
        print(f"CSV file already exists at {file_path}")