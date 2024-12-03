lines = open("day3.txt").read().strip()


pattern = "mul("
N = []
for i in range(len(lines)):
  if lines[i:i+4] == "mul(":
    numbers = []
    j = 0
    while (lines[i+4+j] != ")" and lines[i+4+j] in "0123456789,"):
      numbers.append(lines[i+4+j])
      j += 1
    if lines[i+4+j] == ")" and  "," in numbers:
      numbers = ("").join(numbers)
      N.append(numbers)
  elif lines[i:i+4] == "do()":
    N.append(1)
  elif lines[i:i+7] == "don't()":
    N.append(0)


result = 0 
add = True 
for n in N:
  if n == 0: 
    add = False
  elif n == 1: 
    add = True
  elif add:
    temp = n.split(",") 
    result += int(temp[0]) * int(temp[1])
  else:
    continue



print(result)

