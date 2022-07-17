f = open("Day 10\input.txt")

rules1 = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

rules2 = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

points = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

found = []
incomplete = []
for x in f:
  valid = True
  should_be = ''
  stack = []
  for sym in x:
    if sym in rules1:
      stack.append(sym)
    elif sym in rules2:
      if stack[-1] == rules2[sym]:
        stack.pop(-1)
      else:
        if x not in incomplete:
          valid = False
        should_be = rules1[stack[-1]]
        break
  if valid:
    incomplete.append(stack)
a_score = 0
total_score = 0

finals = []

for i in incomplete:
  total_score = 0
  for x in reversed(i):
    symbol = rules1[x]
    a_score = total_score * 5 + points[symbol]
    total_score = a_score
  finals.append(total_score)

print(sorted(finals)[int(len(finals)/2)])