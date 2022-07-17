import time
start_time = time.time()
f = open("input.txt")

letters = ['a','b','c','d','e','f','g']

def findNum(arr, length):
  for i in arr:
    if len(i) == length:
      return i

def isIn(ele, arr):
  for i in arr:
    for c in i:
      if ele == c:
        return True
  return False

def findNum2(arr, length, letters):
  for i in arr:
    if len(i) == length and letters[0] in i and letters[1] in i and letters[2] in i:
      return i

def findMapping(arr, r, p):
  used = []
  map = [[' ' for i in range(6)] for j in range(7)]

  map[1][5] = findNum(arr, 2)[r]
  used.append(map[1][5])
  map[4][5] = findNum(arr, 2)[p]
  used.append(map[4][5])
  
  for i in findNum(arr, 3):
    if not isIn(i, map):
      map[0][1] = i
      used.append(map[0][1])

  smth = findNum2(arr, 5, (map[1][5], map[4][5], map[0][1]))
  four = findNum(arr, 4)

  for y in used:
    if y in smth:
      smth = smth.replace(y, "")
    if y in four:
      four = four.replace(y, "")

  sm = sorted(smth)
  fo = sorted(four)

  for i in sm:
    if i in fo:
      map[3][1] = i
      used.append(map[3][1])
  
  sm.remove(map[3][1])
  fo.remove(map[3][1])

  map[6][1] = sm[0]
  used.append(map[6][1])
  map[1][0] = fo[0]
  used.append(map[1][0])

  for i in letters:
    if i not in used:
      map[4][0] = i
  
  return map

  
final = 0

for x in f:
  new_keys = {}
  arr = x.replace("\n", "").split(" | ")
  signals = arr[0].split(" ")
  outputs = arr[1].split(" ")

  map = findMapping(signals, 0, 1)
  
  string = ""

  string = map[0][1] + map[1][5] + map[4][5] + map[6][1] + map[4][0] + map[1][0] + map[3][1]
  new_keys[string] =  8
  string = map[0][1] + map[1][0] + map[3][1] + map[4][5] + map[6][1]
  new_keys[string] = 5
  string = map[0][1] + map[1][5] + map[3][1] + map[4][0] + map[6][1]
  new_keys[string] = 2
  string = map[0][1] + map[1][5] + map[3][1] + map[4][5] + map[6][1]
  new_keys[string] = 3
  string = map[0][1] + map[1][5] + map[4][5]
  new_keys[string] = 7
  string = map[0][1] + map[1][5] + map[4][5] + map[6][1] + map[1][0] + map[3][1]
  new_keys[string] = 9
  string = map[0][1] + map[1][0] + map[4][0] + map[6][1] + map[4][5] + map[3][1]
  new_keys[string] = 6
  string = map[1][0] + map[3][1] + map[1][5] + map[4][5]
  new_keys[string] = 4
  string = map[0][1] + map[1][5] + map[4][5] + map[6][1] + map[4][0] + map[1][0]
  new_keys[string] = 0
  string = map[1][5] + map[4][5]
  new_keys[string] = 1

  output = ""


  for z in outputs:
    for i in new_keys:
      if sorted(i) == sorted(z):
        output += str(new_keys[i])
  
  if not len(output) == 4:
    new_keys = {}
    output = ""
    map = findMapping(signals, 1, 0)
  
    string = ""

    string = map[0][1] + map[1][5] + map[4][5] + map[6][1] + map[4][0] + map[1][0] + map[3][1]
    new_keys[string] =  8
    string = map[0][1] + map[1][0] + map[3][1] + map[4][5] + map[6][1]
    new_keys[string] = 5
    string = map[0][1] + map[1][5] + map[3][1] + map[4][0] + map[6][1]
    new_keys[string] = 2
    string = map[0][1] + map[1][5] + map[3][1] + map[4][5] + map[6][1]
    new_keys[string] = 3
    string = map[0][1] + map[1][5] + map[4][5]
    new_keys[string] = 7
    string = map[0][1] + map[1][5] + map[4][5] + map[6][1] + map[1][0] + map[3][1]
    new_keys[string] = 9
    string = map[0][1] + map[1][0] + map[4][0] + map[6][1] + map[4][5] + map[3][1]
    new_keys[string] = 6
    string = map[1][0] + map[3][1] + map[1][5] + map[4][5]
    new_keys[string] = 4
    string = map[0][1] + map[1][5] + map[4][5] + map[6][1] + map[4][0] + map[1][0]
    new_keys[string] = 0
    string = map[1][5] + map[4][5]
    new_keys[string] = 1

    output = ""


    for z in outputs:
      for i in new_keys:
        if sorted(i) == sorted(z):
          output += str(new_keys[i])

  final += int(output)

print(final)