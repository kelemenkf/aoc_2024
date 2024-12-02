import copy 

lines = open("day2.txt", "r").read()
lines = lines.strip().split("\n")
lines = [line.split() for line in lines]
lines = [[int(x) for x in line] for line in lines]


def isIncreasing(level):
  increasing = True
  for i in range(len(level)-1):
    if level[i] >= level[i+1]:
      increasing = False 
  return increasing 
   

def isDecreasing(level):
  decreasing = True 
  for i in range(len(level) - 1):
    if level[i] <= level[i+1]:
      decreasing = False 
  return decreasing 



def difference(level):
  safe = True 
  for i in range(len(level) - 1):
    diff = abs(level[i] - level[i+1])   
    if diff < 1 or diff > 3:
      safe = False 
  return safe 
      


def removeOne(level, i):
  newlevel = copy.deepcopy(level)  
  newlevel.pop(i)
  return newlevel



safe = 0 
for line in lines: 
  if (isIncreasing(line) or isDecreasing(line)) and difference(line):
    safe += 1
  else: 
    for i in range(len(line)):
      newline = removeOne(line, i)
      if (isIncreasing(newline) or isDecreasing(newline)) and difference(newline): 
        safe += 1 
        break 



print(safe)
