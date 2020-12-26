# Breadth First Search
# Time Complexity: O(V+E)
#
#	Using Adjacency List
#	Example: graph = { 0: [1], 1: [2,3], 2: [0, 1]}
def bfs(graph, N):
	queue = [0]
	visited = [ False for i in range(N)]

	while len(queue) > 0:
		next_node = queue.pop(0)
		visited[next_node] = True

		neighbours = graph[next_node]
		for nei in neighbours:
			if !visited[nei]:
				queue.append(nei)