import sys

f = open("Day 4/input.txt", "r")
first = f.readline()

drawn = first.replace("\n", "").split(",")

def isWinner(arr):
  cols = []
  for i in arr:
    if i == ["X", "X", "X", "X", "X"]:
      return True
  for col in range(5):
    for row in arr:
      cols.append(row[col])
    if cols == ["X", "X", "X", "X", "X"]:
      return True
    cols = []
  return False

def unMarkedCount(board):
  counter = 0
  for row in board:
    for col in row:
      if col != "X":
          counter+=int(col)
  return counter

def search(arr, ele):
  for a in range(len(arr)):
    for b in range(5):
      if arr[a][b] == ele:
        return a,b
  return -1,-1

def printBoard(arr):
  for a in arr:
    for b in a:
      for c in b:
        print(c, end=" ")
      print()
    print()

stuff = []

for x in f:
  line = x.replace("\n", "").split(" ")
  line = list(filter(('').__ne__, line))
  if len(line) != 0:
    stuff.append(line)

counter = 0
boards = []
anArray = []

for i in stuff:
  anArray.append(i)
  counter+=1
  if counter % 5 == 0:
    boards.append(anArray)
    counter = 0
    anArray = []

wins = []

for play in drawn:
  for board in range(len(boards)):
    p = search(boards[board], play)
    if p != (-1,-1):
      boards[board][p[0]][p[1]] = "X"
    if isWinner(boards[board]) and board not in wins:
      wins.append(board)
    if len(wins) == len(boards):
      print("Board {} finally won, with the winning number of {}".format(wins[-1], play))
      sum = unMarkedCount(boards[board])
      print(sum*int(play))
      sys.exit()