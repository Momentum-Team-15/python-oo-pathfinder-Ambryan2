from ast import Compare
import numbers
import random
from sqlite3 import Row
from statistics import mean

# reads file 
f = open('test.txt', 'r')
file = f.read()

# want to split on new line NOTE (new line = y) (new number = x)
all_values = file.split('\n')
rows = []
columns = []

for number in file.split('\n'):
    rows.append(number.split())

# this is because file has an empty line
rows.pop()

for number in range(0,len(rows[0])):
    temp = ['border']
    for row in rows:
        temp.append(row[number])
    temp.append('border')
    columns.append(temp)

class Paths:
    def __init__(self):
        self.shortest_path = []
        self.paths = []
        self.path_avg = []
        self.shortest_avg = 0
    
    def make_paths(self, x, y):
        number = int(columns[x][y+1])
        # print(f"number in location is {number}")
        number_in_path = [number]
        path = [(x,y)]
        differences_in_path = []

        # loop to go to end of array
        for justletters in range(0,len(rows)):
            # need to make x and y variables reusable
            number = int(columns[x][y+1])
            # this will find number and will need to be repeated
            compare = []
            for option in range(0,3):
                compare.append(columns[x+1][(y) + option])
            #This makes an array with the differences in the found numbers
            differences = []
            for value in compare:
                if value != 'border':
                    differences.append(int(abs((number) - int(value))))
                else: 
                    differences.append(number + 1000)
            # this pick from the differences array and then returns the location of number
            y_possible = []
            count = 0

            # new_y = 0
            for choices in differences:
                if choices == min(differences):
                    y_possible.append(y + count)
                count += 1
            # randomly selects location from possible location
            new_number = random.choice(range(0,len(y_possible)))
            
            # gives location of the new number selected
            x +=  1
            y = y_possible[new_number]-1

            number_in_path.append(columns[x][y+1])
            path.append((x,y))
            differences_in_path.append(min(differences))
        
        path_avg = mean(differences_in_path)
        self.paths.append(path)
        self.path_avg.append(path_avg)

    def shortest(self):
        locator = self.path_avg.index(min(self.path_avg))
        self.shortest_path.append(self.paths[locator])
        self.shortest_avg = self.path_avg[locator]

y_used = 0

trecker = Paths()
for paths in range(0,len(columns)-2):
    trecker.make_paths(0,y_used)
    y_used += 1

trecker.shortest()
print(f"Path with least elevation change of {round(trecker.shortest_avg)}")
