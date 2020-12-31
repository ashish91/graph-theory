# Lazy Dijkstra
# adjlist = (weight, to)
# Time: Elog(V)
def dijkstra(start, adjlist, N):
	dist = [float('inf') for i in range(N)]
	dist[start] = 0

	pq = heappq.heapify([(0, start)])
	visited = {}
	while len(pq) > 0:
		weight, node = heappq.heappop()
		visited[node] = True

		# The value in heap is outdated and there
		# is a shorter path as per dist so no need
		# to compute on basis of outdated weight
		if dist[node] < weight: continue

		neighbours = adjlist[node]
		for nei_weight, nei in neighbours:
			if nei not in visited:
				# We don't use weight from heap because
				# dist contains the most updated distance for node
				nei_dist = nei_weight + dist[node]

				# Relax edges
				if nei_dist < dist[nei]:
					dist[nei] = nei_dist
					# Duplicates with same node but
					# different weight can exist
					heappq.heappush((nei_weight, nei))

	return dist

# Lazy Dijkstra
# adjlist = (weight, to)
# Time: Elog(V)
def dijkstra(start, adjlist, N):
	dist = [float('inf') for i in range(N)]
	dist[start] = 0

	# Use indexed priority queue to update
	# the values with updated distance
	pq = heappq.heapify([(0, start)])
	visited = {}
	while len(pq) > 0:
		weight, node = heappq.heappop()
		visited[node] = True

		# The value in heap is outdated and there
		# is a shorter path as per dist so no need
		# to compute on basis of outdated weight
		if dist[node] < weight: continue

		neighbours = adjlist[node]
		for nei_weight, nei in neighbours:
			if nei not in visited:
				# We don't use weight from heap because
				# dist contains the most updated distance for node
				nei_dist = nei_weight + dist[node]

				# Relax edges
				if nei_dist < dist[nei]:
					dist[nei] = nei_dist
					if heappq.heapcontains(nei):
						heappq.heapupdate((nei_weight, nei))
					else:
						heappq.heappush((nei_weight, nei))

	return dist