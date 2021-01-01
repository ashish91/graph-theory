def topological_sort(glist, N):
  topological_sorted = []
  visited = {}
  def dfs(node, glist):
    nonlocal topological_sorted
    nonlocal visited

    visited[node] = True
    for nei, weight in glist[node]:
      if nei not in visited:
        dfs(nei)

    topological_sorted.insert(0, node)

  for i in range(N):
    if i not in visited:
      dfs(i, glist)

  return topological_sorted

# Single Shortest path in a DAG
# Time: O(V+E)
def single_shortest_path_dag(src, dest, glist, N):
  dist = [None for i in range(N)]
  dist[src] = 0

  topsort = topological_sort(glist, N)
  for i in range(N):
    node = topsort[i]

    if dist[node] is not None:
      neighbours = glist[node]

      for nei, weight in neighbours:
        if dist[nei] is None:
          dist[nei] = weight
        else:
          dist[nei] += weight

  return dist
