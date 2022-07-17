f = open("C:/Users/thiru/Documents/VSCodeProjects/Advent of Code 2021/Day 1/input.txt", "r")

depths = []

counter = 0

for x in f:
  depths.append(int(x))

sums = []

for i in range(len(depths)-2):
  sums.append(depths[i] + depths[i+1] + depths[i+2])

sumss = 0

for i in range(len(sums)-1):
  if sums[i+1] > sums[i]:
    sumss += 1

print(sumss)