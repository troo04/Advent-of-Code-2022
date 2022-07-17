f = open("Day 3\input.txt", "r")

def most_common(arr, col):
  zero_counter = 0
  one_counter = 0
  for element in arr:
    if element[col] == "0":
      zero_counter += 1
    elif element[col] == "1":
      one_counter += 1
  return zero_counter, one_counter

def remove(arr, bit, col):
  for index in range(len(arr)):
    if arr[index][col] == bit:
      arr[index] = "aaaaaaaaaaaaaaaaa"

def check(arr):
  counter = 0
  for i in arr:
    if i != "aaaaaaaaaaaaaaaaa":
      counter += 1
  if counter > 1:
    return False
  else:
    return True

data = []

for x in f:
  data.append(x.replace("\n", ""))
f.close()

for col in range(len(data[0])):
  counters = most_common(data, col)
  if counters[0] > counters[1]:
    remove(data, "1", col)
  else:
    remove(data, "0", col)

for i in data:
  if i != "aaaaaaaaaaaaaaaaa":
    bin = i

oxygen = int(bin, 2)

f = open("Day 3\input.txt", "r")

data = []

for x in f:
  data.append(x.replace("\n", ""))

for col in range(len(data[0])):
  if check(data):
    break
  counters = most_common(data, col)
  if counters[0] <= counters[1]:
    remove(data, "1", col)
  else:
    remove(data, "0", col)

for i in data:
  if i != "aaaaaaaaaaaaaaaaa":
    bin = i

carbon = int(bin, 2)

print(oxygen * carbon)