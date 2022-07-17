import sys

f = open("Day 11\input.txt", "r")

model = []
line = []
octipi = []

def surroundings(map, point):
    exists = []

    if point[0]-1 >= 0 and point[0]-1 < len(map):
        exists.append((point[0]-1, point[1]))
    if point[0]+1 >= 0 and point[0]+1 < len(map):
        exists.append((point[0]+1, point[1]))
    if point[1]-1 >= 0 and point[1]-1 < len(map[0]):
        exists.append((point[0], point[1]-1))
    if point[1]+1 >= 0 and point[1]+1 < len(map[0]):
        exists.append((point[0], point[1]+1))

    # diagonals
    if (point[0]-1 >= 0 and point[1]-1 >= 0) and (point[0]-1 < len(map[0]) and point[1]-1 < len(map[0])):
        exists.append((point[0]-1, point[1]-1))
    if (point[0]-1 >= 0 and point[1]+1 >= 0) and (point[0]-1 < len(map[0]) and point[1]+1 < len(map[0])):
        exists.append((point[0]-1, point[1]+1)) 
    if point[0]+1 >= 0 and point[1]-1 >= 0 and (point[0]+1 < len(map[0]) and point[1]-1 < len(map[0])):
        exists.append((point[0]+1, point[1]-1))
    if point[0]+1 >= 0 and point[1]+1 >= 0 and (point[0]+1 < len(map[0]) and point[1]+1 < len(map[0])):
        exists.append((point[0]+1, point[1]+1))

    return exists

def findSim(model):
    counter = 0
    for row in model:
        for col in row:
            if col == 0:
                counter += 1

    if counter == len(model) * len(model):
        return True
    return False

def count(model):
    counter = 0
    for row in model:
        for col in row:
            if col == 0:
                counter += 1
    
    return counter

def findFlashy(model):
    flasheys = []

    for row in range(len(model)):
        for col in range(len(model[row])):
            if model[row][col] > 9:
                flasheys.append((row, col))

    return flasheys

flasheys = findFlashy(model)

def flash(model, point):
    exist = surroundings(model, point)
    
    flasheys.append(point)
    for i in exist:
        model[i[0]][i[1]] += 1
    
    for row in range(len(model)):
        for col in range(len(model)):
            if model[row][col] > 9 and (row, col) not in flasheys:
                octipi.append((row, col))
                flash(model, (row, col))
            

for x in f:
    line = []
    for y in x:
        if not y == "\n":
            line.append(int(y))
    model.append(line)

flashes = 0

x = 0

while True:
    octipi = []
    flasheys = []
    # increments everything by 1
    for row in range(len(model)):
        for col in range(len(model[row])):
            model[row][col] += 1

    #flashing stuff
    for row in range(len(model)):
        for col in range(len(model[row])):
            if model[row][col] > 9 and (row, col) not in octipi:
                octipi.append((row, col))
                flash(model, (row,col))

    flasheys1 = findFlashy(model)
    for i in flasheys1:
        model[i[0]][i[1]] = 0
    
    flashes += count(model)
    
    if findSim(model):
        print("Step", x+1)
        sys.exit()
    
    x+=1
