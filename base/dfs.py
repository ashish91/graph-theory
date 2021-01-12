# Depth First Search
# Time Complexity: O(V+E)
#
#  Using Adjacency List
#  Example: graph = { 0: [1], 1: [2,3], 2: [0, 1]}

def dfs_recursive(graph, N):
  visited = [ False for i in range(N)]
  start = 0
  def dfs(node, graph, visited):
    if visited[node]:
      return

    visited[node] = True
    for neighbour in graph[node]:
      dfs(neighbour, graph, visited)

  dfs(start, graph, visited)