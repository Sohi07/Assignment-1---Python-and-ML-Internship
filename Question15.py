import csv

with open('Ques15.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
