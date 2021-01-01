# Find Cycle
# Time Complexity: O(V+E)
#
#  Using Adjacency List
#  Example: graph = { 0: [1], 1: [2,3], 2: [0, 1]}
def dfs(graph, node, visited, seen):
  neighbours = graph[node]
  visited[node] = True
  seen[node] = True

  for nei in neighbours:
    if !visited[nei]:
      # If True then cycle exists and return
      if dfs(graph, nei, visited, seen):
        return True
    elif seen[node]:
      return True

  seen[node] = False

def find_cycle(graph, N):
  visited = [False for i in range(N)]
  seen = [False for i in range(N)]

  for i in range(N):
    if !visited[i]:
      if dfs(graph, i, visited, seen):
        return True