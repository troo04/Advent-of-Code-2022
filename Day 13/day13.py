import sys

f = open("Day 13\input.txt", "r")

dots = []
folds = []

for line in f:
    if line[0] != 'f' and line[0] != '\n':
        dots.append(line.replace("\n", "").split(","))
    elif line[0] == 'f':
        folds.append(line[11:].replace("\n", "").split("="))

for dot in range(len(dots)):
    dots[dot][0] = int(dots[dot][0])
    dots[dot][1] = int(dots[dot][1])

for fold in folds:
    oldDots = []
    if fold[0] == 'y':
        for dot in dots:
            if dot[1] > int(fold[1]):
                diff = dot[1]-int(fold[1])
                if [dot[0], int(fold[1]) - diff] not in dots:
                    dots.append([dot[0], int(fold[1]) - diff])
                oldDots.append(dot)
    elif fold[0] == 'x':
        for dot in dots:
            if dot[0] > int(fold[1]):
                diff = dot[0]-int(fold[1])
                if [int(fold[1]) - diff ,dot[1]] not in dots:
                    dots.append([int(fold[1]) - diff ,dot[1]])
                oldDots.append(dot)
    for element in oldDots:
        if element in dots:
            dots.remove(element)

graph = []

for a in range(6):
    n_temp = []
    for b in range(40):
        n_temp.append(0)
    graph.append(n_temp)


for dot in dots:
    graph[dot[1]][dot[0]] = 1

for row in graph:
    for col in row:
        if col == 1:
            print('#', end="")
        else:
            print(' ', end="")
    print()