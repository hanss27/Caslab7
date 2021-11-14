import os, sys, csv

#Load Database
file = open('tes.csv')
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
first = []
a = [['2021-10-05',100,'a'], ['2021-10-05',300,'b'],['2021-10-05',10,'c']]

# for a in rows:
#     income.append(a[2:len(a)][:])

# for a in rows:
#     first.append(a[0:3][:])
# count = 0
# for i in income:
#         for a in i:
#             first[count].append(a)
#         count += 1
