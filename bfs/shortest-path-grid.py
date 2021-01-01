# Given a matrix with 1's and 0's where
#   1 - Movable path
#   0 - Rocks in the path
# Shortest path from (r1,c1) to (r2,c2)

def shortest_path_grid(grid, r1, c1, r2, c2):
  M = len(grid)
  N = len(grid[0])

  directions = [(-1,0),(0,-1),(1,0),(0,1)]
  queue = [(r1,c1)]
  visited = {(r1,c1): True}

  path = 0
  while len(queue) > 0:
    r,c = queue.pop()

    if r == r2 and c == c2:
      return path
    for dir in directions:
      x,y = r+dir[0], c+dir[1]
      if x >= 0 and x < M and y >= 0 and y < N and !visited[(x,y)] and grid[x][y] != 0:
        queue.append((x,y))

    path += 1

  return -1
