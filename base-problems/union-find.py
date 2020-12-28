def union_find(size):
	num_components = size

	parent = [i for i in range(size)]
	size_components = [1 for i in range(size)]

	def unify(node1, node2):
		root1 = find(node1)
		root2 = find(node2)

		# Same root means they are connected
		if root1 == root2:
			return True

		# Merge smaller component into bigger one
		if size_components[root1] < size_components[root2]:
			size_components[root2] += size_components[root1]
			parent[root1] = root2
		else:
			size_components[root1] += size_components[root2]
			parent[root2] = root1

		# Merging reduces component by 1
		num_components -= 1
		return True


	def find(node):
		nonlocal parent

		root = node
		# Find the topmost root
		while root != parent[root]:
			root = parent[root]

		# Path compression
		# In parent update all ancestor's parent
		# as the topmost root
		while node != root:
			temp = parent[node]
			parent[node] = root
			node = temp

		return root