import csv
import os


def update_status(requirement_id, testcase_id, status):
    file_path = './credentials/cloudxwebtestcases.csv'
    print("h3")
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0].strip() == requirement_id and row[1].strip() == testcase_id:
            row[11] = status

    with open('./credentials/cloudxwebtestcases.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def read_and_split_csv(requirement_id, testcase_id):
    filename = './credentials/cloudxwebtestcases.csv'

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].strip() == requirement_id and row[1].strip() == testcase_id:
                specific_column_value = row[5]
                return specific_column_value.split(',')
                # print(specific_column_value.split(',')[0])

