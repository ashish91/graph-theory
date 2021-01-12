def floyd_warshall(matrix):
  N = len(matrix)
  dist = [[None for c in range(N)] for r in range(N)]
  path = [[None for c in range(N)] for r in range(N)]

  # Initializes distance matrix as the graph
  # meaning the distance are direct paths
  for u in range(N):
    for v in range(N):
      dist[u][v] = matrix[u][v]
      if matrix[u][v] != float('infinity'):
        path[u][v] = v

  for k in range(N):
    for u in range(N):
      for v in range(N):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
          # i -> j
          # breaks to
          # i -> k -> j
          path[i][j] = path[i][k]

  return dp