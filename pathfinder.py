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
    temp = []
    for row in rows:
        temp.append(row[number])
    columns.append(temp)

# this determines location and the 3 adjacent
def location(x,y):
    number = rows[y][x]
    print(f"number in location is {number}")
    compare = []
    for number in range(0,3):
        compare.append(columns[x+1][(y+1) - number])
    print(f"{compare}")




# TODO make an element in first row the starting position
# TODO Determine the column to right numbers right, right-up, and right-down
# TODO make position move into that piece 

location(4,4)
print(file)
print()
print(columns)


# print(new_rows)
# print(row_length)
# example for loop
# [letter for letter in file]