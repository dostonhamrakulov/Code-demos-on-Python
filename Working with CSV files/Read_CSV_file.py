# importing csv module
import csv

# csv file name
filename = "Students.csv"

# initializing the titles and rows list
fields = []
rows = []
small_dict = {}
large_dict = {}
list_ = []


# converting csv data to dictionary
reader = csv.DictReader(open("Students.csv", "r"))
for line in reader:
    list_.append(line)
print("============== Dictionary ====================")
print(list_)


# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

# getting specific row, here only the first row
for row in rows[:1]:
    for col in row:
        fields.append(col)
print("================== Row 1 =============== ")
print(fields)

print('================== First 5 rows are: ===================')
fields.clear()
for row in rows[1:5]:
    # parsing each column of a row
    for col in row:
        fields.append(col)
    print("----- ROW ------")
    print(fields)
    fields.clear()
    # print('\n')


