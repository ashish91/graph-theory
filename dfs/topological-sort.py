def topological_sort(glist, N):
  topological_sorted = []
  visited = {}
  def dfs(node, glist):
    nonlocal topological_sorted
    nonlocal visited

    visited[node] = True
    for nei in glist[node]:
      if nei not in visited:
        dfs(nei)

    topological_sorted.insert(0, node)

  for i in range(N):
    if i not in visited:
      dfs(i, glist)

  return topological_sorted