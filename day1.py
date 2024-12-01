lines = open("day1.txt", "r").read()
lines = lines.strip().split("\n")

left = []
right = []
for line in lines:
  line = line.split()
  left.append(int(line[0]))
  right.append(int(line[1]))



left = sorted(left)
right = sorted(right)


result = 0
if (len(left) == len(right)):
  for i in range(len(left)):
    result += abs(left[i] - right[i])



similarity_score = 0
for i in range(len(left)):
  if left[i] in right: 
    similarity_score += left[i] * right.count(left[i])

print(result)
print(similarity_score)
