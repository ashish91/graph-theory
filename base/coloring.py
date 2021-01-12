# Backtracking algorithm for coloring graph
# Given m colors and n nodes
#
# Time: O(n^m) => n nodes can be colored with m colors each
def coloring(adjlist, N, M):
  colored = [None] * N

  def color(node, adjlist, N, M):
    nonlocal colored
    nonlocal all_colored

    if node == N:
      all_colored = True
      return True

    for c in range(M):
      if (is_safe(node,c)):
        colored[node] = c
        return color(node+1, adjlist, N, M)

    return False

  def is_safe(node, c, adjlist):
    for nei in adjlist[node]:
      if color[nei] == c:
        return False

    return True

  if color(0, adjlist, N, M):
    return colored
  else:
    return None
