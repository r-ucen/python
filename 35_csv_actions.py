# csv files
import csv

with open("examples/exampleCSV.csv","r",encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    print(type(csv_reader))

    # skipping column names
    next(csv_reader)
    for row in csv_reader:
        print(row)

'''
<class '_csv.reader'>
['Petr', 'Novák', '1976', 'pnovak@utb.cz']
['Aleš', 'Navrátil', '1975', 'anavratil@utb.cz']
['Viktor', 'Nový', '1981', 'vnovy@utb.cz']
['Karel', 'Novotný', '1990', 'knovotny@gmail.com']
['Václav', 'Nejedlý', '1976', 'vnejedly@centrum.cz']
'''

# extract only one column
with open("examples/exampleCSV.csv","r",encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    print(type(csv_reader))
    next(csv_reader)
    for row in csv_reader:
        print(row[1])

'''
<class '_csv.reader'>
Novák
Navrátil
Nový
Novotný
Nejedlý
'''

# load the csv file into a dictionary
with open('examples/exampleCSV.csv','r', encoding = "utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

'''
{'jméno': 'Petr', 'příjmení': 'Novák', 'rok': '1976', 'email': 'pnovak@utb.cz'}
{'jméno': 'Aleš', 'příjmení': 'Navrátil', 'rok': '1975', 'email': 'anavratil@utb.cz'}
{'jméno': 'Viktor', 'příjmení': 'Nový', 'rok': '1981', 'email': 'vnovy@utb.cz'}
{'jméno': 'Karel', 'příjmení': 'Novotný', 'rok': '1990', 'email': 'knovotny@gmail.com'}
{'jméno': 'Václav', 'příjmení': 'Nejedlý', 'rok': '1976', 'email': 'vnejedly@centrum.cz'}
'''

# extract only one column from the dictionary
with open('examples/exampleCSV.csv','r', encoding = "utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['příjmení'])

'''
Novák
Navrátil
Nový
Novotný
Nejedlý
'''
# to write into the csv
with open("examples/exampleCSV.csv","a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Petr","Nikdo",1975,"nikdo@gmail.com"])

# OR LIKE THIS 
    
with open("examples/exampleCSV2.csv","w",newline='') as csv_file:
    fieldnames = ["Jméno","Příjmení","rok","email"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({"Jméno":"Petr","Příjmení":"Novák","rok":1945,"email":"novak@gmail.com"})