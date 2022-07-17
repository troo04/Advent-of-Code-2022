f = open("Day 9\input.txt", "r")

map = []

for x in f:
    row = []
    for i in x:
        if i != "\n":
            row.append(int(i))
    map.append(row)

low = 0
risk = 0

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

  return exists

dups = []

def findAllPoints(arr, pos):
  area = 0
  for point in arr:
    if not map[point[0]][point[1]] == 9:
      if map[point[0]][point[1]] > map[pos[0]][pos[1]] and (point[0], point[1]) not in dups:
        area += 1
        #print(point[0], point[1])
        dups.append((point[0], point[1]))
        findAllPoints(surroundings(map, (point[0], point[1])), (point[0], point[1]))
  return len(dups) + 1

def isLowPoint(exists, map):
  counter = 0

  for x in exists:
      if map[x[0]][x[1]] > map[a][b]:
        counter += 1

  if counter == len(exists):
    return True, exists
  
  return False, exists

counter = 0
basins = []
for a in range(len(map)):
  for b in range(len(map[a])):
    exists = surroundings(map, (a, b))

    if isLowPoint(exists, map)[0]:
      basins.append(findAllPoints(exists, (a, b)))
    dups = []

basins.sort()
print(int(basins[len(basins)-1]) * int(basins[len(basins)-2]) * int(basins[len(basins)-3]))