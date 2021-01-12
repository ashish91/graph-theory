# Time Complexity: O(EV)
def bellman_ford(S, edgelist, N):
  dist = [float('infinity')] * N
  dist[S] = 0

  # For each vertice
  for v in range(N):
    # Relax all edges
    for edge in edgelist:
      if dist[edge.fro] + edge.weight < edge.to:
        dist[edge.to] = dist[edge.fro] + edge.weight

  # Find neg cycles. If a node is part
  # of neg cycle then dist will be less than
  # the optimal solution
  for v in range(N):
    for edge in edgelist:
      if dist[edge.fro] + edge.weight < edge.to:
        dist[edge.to] = float('-infinity')

  return dist


