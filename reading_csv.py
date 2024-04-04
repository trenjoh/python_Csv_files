#importing  using  reader
from csv import reader
with open("1.1 fighters.csv.csv") as file:
    csv_reader = reader(file )
    # for row in csv_reader:
    #     print(row)
    next(csv_reader) # if you don't the header
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter [1]} adress {fighter[2]}")

# using dict reader
# has ordered dictionaries

from csv import DictReader
with open("1.1 fighters.csv.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['Name'])
