import csv

file_name = "person_information.csv"

with open(file_name, 'r') as csv_file:
    # get csv delimeter
    csv_delimiter = str(csv.Sniffer().sniff(csv_file.readline()).delimiter)
    # read csv with delimter
    csv_reader = csv.reader(csv_file, delimiter=csv_delimiter)

AGE_COL = 8
# write data into csv file
fields = ['Name', 'Branch', 'Year', 'CGPA']
# append header
col_nums = len(fields)
while(col_nums < AGE_COL - 1):
    fields.append('')
    col_nums += 1
else:
    fields.append("Age")

# list data
rows = [
    ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]

fields_dict = ['name', 'branch', 'year', 'cgpa']
# dict data
mydict = [
    {'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
    {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
    {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
    {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
    {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}
]

# writing to csv file
with open(file_name, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=csv_delimiter)
    csvwriter.writerow(fields)  # write header file
    csvwriter.writerows(rows)   # writing the data rows

with open(file_name, 'a', newline='') as csvfile:
    # creating a csv dict writer object
    csvwriter = csv.DictWriter(csvfile, fieldnames = fields_dict, delimiter=csv_delimiter)
    # writer.writeheader()  # if header not exist
    csvwriter.writerows(mydict) # write data