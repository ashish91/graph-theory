# Eager Prim MST
# Using Adjacency Matrix
# Time: O(V^2)

def min_node(dist, mst_set, N):
  min_weight = float('inf')
  for i in range(N):
    if min_weight > dist[i] and not mst_set[i]:
      min_weight = dist[i]
      min_vertex = i

  return min_vertex


def prim_mst(gmatrix, N):
  dist = [float('inf')]*N
  mst_set = [False]*N

  parent = [-1]*N

  for _ in range(N):
    u = min_node(dist, mst_set)
    mst_set[u] = True

    for v in range(N):
      if gmatrix[u][v] != 0 and gmatrix[u][v] < dist[v] and not mst_set[v]:
        dist[v] = gmatrix[u][v]
        parent[v] = u

  return parent


# Lazy version Prim's MST
# Using Adjacency List
# Time: O(Elog(E))

def prim_mst(glist, N):

  heap = []
  buildheap(heap, graph)

  visited = {}
  while len(heap) > 0:
    edge = heapq.heappop(heap)
