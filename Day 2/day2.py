f = open("C:/Users/thiru/Documents/VSCodeProjects/Advent of Code 2021/Day 2/input.txt", "r")

direct = []

for x in f:
  direct.append(x.replace("\n", ""))

forward = 0
aim = 0
depth = 0

for i in direct:
  y = i.split(" ")
  if y[0] == 'forward':
    forward+=int(y[1])
    depth = depth + (aim * int(y[1]))
  elif y[0] == "up":
    aim-=int(y[1])
  elif y[0] == "down":
    aim+=int(y[1])

print(forward * depth)