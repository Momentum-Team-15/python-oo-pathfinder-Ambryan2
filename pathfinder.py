from ast import Compare
import numbers
import random
from sqlite3 import Row

# reads file 
f = open('test.txt', 'r')
file = f.read()

# want to split on new line NOTE (new line = y) (new number = x)
all_values = file.split('\n')
rows = []
columns = []

for number in file.split('\n'):
    rows.append(number.split())

for number in range(0,len(rows[0])):
    temp = ['border']
    for row in rows:
        temp.append(row[number])
    temp.append('border')
    columns.append(temp)

# this determines location and the 3 adjacent
def location(x,y):
    number = columns[x][y+1]
    print(f"number in location is {number}")
    # this will find number
    compare = []
    for number in range(0,3):
        compare.append(columns[x+1][(y) + number])

    print(f"{compare}")




# TODO make an element in first row the starting position
# TODO Determine the column to right numbers right, right-up, and right-down
# TODO make position move into that piece 

location(0,0)
print(columns)
print()
# print(columns)


# print(new_rows)
# print(row_length)
# example for loop
# [letter for letter in file]