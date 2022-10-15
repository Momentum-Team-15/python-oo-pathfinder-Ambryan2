from ast import Compare
import numbers
import random
from sqlite3 import Row
from statistics import mean

# reads file 
f = open('elevation_small.txt', 'r')
file = f.read()

# want to split on new line NOTE (new line = y) (new number = x)
all_values = file.split('\n')
rows = []
columns = []

for number in file.split('\n'):
    rows.append(number.split())

rows.pop()

for number in range(0,len(rows[0])):
    temp = ['border']
    print(number)
    for row in rows:
        temp.append(row[number])
    temp.append('border')
    columns.append(temp)

print(len(rows))
print(len(columns))