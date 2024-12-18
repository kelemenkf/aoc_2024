import numpy as np
np.set_printoptions(threshold=np.inf)


lines = open("day6.txt", "r").read()
grid = lines.strip().split('\n')
grid = [list(row) for row in grid]
grid = np.array(grid)


def get_current_pos(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "^":
        return (i,j)


def check_obstacle(row, col, direction):
  if grid[row-1][col] == "#" and direction == 'u':
    return True
  elif grid[row+1][col] == "#" and direction == 'd':
    return True
  elif grid[row][col-1] == "#" and direction == 'l':
    return True
  elif grid[row][col+1] == '#' and direction == 'r':
    return True
  else:
    return False  



def move(row, col, direction):
  if row > 0 and col > 0 and row < grid.shape[0]-1 and col < grid.shape[1]-1:
     grid[row][col] = 'X'
     if direction == 'u':
      if not(check_obstacle(row, col, direction)):
        grid[row-1][col] = "^"
      else:
        grid[row][col] = "^"
        direction = 'r'
     elif direction == 'r': 
      if not(check_obstacle(row, col, direction)):
        grid[row][col+1] = "^"
      else:
        grid[row][col] = "^"
        direction = 'd'
     elif direction == 'd':
      if not(check_obstacle(row, col, direction)):
        grid[row+1][col] = "^"
      else: 
        grid[row][col] = "^"
        direction = 'l'
     elif direction == 'l':
      if not(check_obstacle(row, col, direction)):
        grid[row][col-1] = "^"
      else: 
        grid[row][col] = "^"
        direction = 'u'
     return direction
     

direction = 'u'
row, col = get_current_pos(grid)
print(grid.shape[0] - 1, grid.shape[1])
while(row > 0 and col > 0 and row < grid.shape[0]-1 and col < grid.shape[1]-1):
  direction = move(row, col, direction)
  row, col = get_current_pos(grid)
  print(row, col)


result = 1 + np.sum(grid == 'X')
print(result)
