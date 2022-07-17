import sys

f = open("Day 5\input.txt")

x_val = 0
y_val = 0

def desperateMeasures(first, second):
    arrayOfStuff = []
    if first[0] > second[0]:
        arrayOfStuff.append(-1)
    elif second[0] > first[0]:
        arrayOfStuff.append(1)
    
    if first[1] > second[1]:
        arrayOfStuff.append(-1)
    elif second[1] > first[1]:
        arrayOfStuff.append(1)
    
    return arrayOfStuff

for x in f:
    line = x.replace("\n", "").replace(" ", "").split("->")
    for y in line:
        if int(y.split(",")[0]) > x_val:
            x_val = int(y.split(",")[0])
        if int(y.split(",")[1]) > y_val:
            y_val = int(y.split(",")[1])

f.close()

grid = []

rows, cols = (1000, 1000)
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(".")
    grid.append(col)

f = open("Day 5\input.txt")

for x in f:
    line = x.replace("\n", "").replace(" ", "").split("->")
    first = tuple(map(int, line[0].split(',')))
    second = tuple(map(int, line[1].split(',')))
    
    if first[0] != second[0] and first[1] != second[1]:
        stuff = desperateMeasures(first, second)
        diff = abs(first[0]-second[0])
        points = (first[0], first[1])
        for i in range(diff+1):
            if grid[points[1]][points[0]] == ".":
                grid[points[1]][points[0]] = "1"
            else:
                grid[points[1]][points[0]] = str(int(grid[points[1]][points[0]])+1)
            points = (points[0]+stuff[0], points[1]+stuff[1])
    elif first[0] == second[0]:
        if first[1] > second[1]:
            diff = first[1] - second[1]
            for i in range(0, diff+1):
                if grid[second[1]+i][second[0]] == ".":
                    grid[second[1]+i][second[0]] = "1"
                else:
                    grid[second[1]+i][second[0]] = str(int(grid[second[1]+i][second[0]]) + 1)
        else:
            diff = second[1] - first[1]
            for i in range(0, diff+1):
                if grid[first[1]+i][first[0]] == ".":
                    grid[first[1]+i][first[0]] = "1"
                else:
                    grid[first[1]+i][first[0]] = str(int(grid[first[1]+i][first[0]]) + 1)
    else:
        if first[0] > second[0]:
            diff = first[0] - second[0]
            for i in range(0, diff+1):
                if grid[second[1]][second[0]+i] == ".":
                    grid[second[1]][second[0]+i] = "1"
                else:
                    grid[second[1]][second[0]+i] = str(int(grid[second[1]][second[0]+i]) + 1)
        else:
            diff = second[0] - first[0]
            for i in range(0, diff+1):
                if grid[first[1]][first[0]+i] == ".":
                    grid[first[1]][first[0]+i] = "1"
                else:
                    grid[first[1]][first[0]+i] = str(int(grid[first[1]][first[0]+i]) + 1)
    

counter = 0
for row in grid:
    for col in row:
        if col != "." and int(col) >= 2:
            counter += 1

print(counter)