import csv 
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

data1 = []
data2 = []
with open(file1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        data1.append(i)

with open(file2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        data2.append(i)

header1 = data1[0]
header2 = data2[0]

p_d1 = data1[1: ]
p_d2 = data2[1: ]

header = header1 + header2

final_d = []

for i in p_d1:
    final_d.append(i)
for j in p_d2:
    final_d.append(j)
with open("total_stars.csv", "w", encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerow(final_d)

df = pd.read_csv('total_stars.csv')