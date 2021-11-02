import os, sys, csv

#Load Database
file = open('income.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
income = []
note = []
a = "tes123456"
print(a[:len(a)-3])
for row in csvreader:
    rows.append(row)
file.close()

for i in rows[0]:
    y = i.split(";")
    income.append(int(y[0]))
    note.append(y[1])   

print(income)
print(note)
