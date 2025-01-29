from collections import defaultdict, deque

def calculate_tree_properties(test_cases):
    results = []
    for test in test_cases:
        V, edges = test
        # Build adjacency list
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        # Function to perform BFS and return the farthest node and its distance
        def bfs(start):
            visited = [-1] * V
            queue = deque([(start, 0)])
            visited[start] = 0
            farthest_node, max_dist = start, 0
            while queue:
                node, dist = queue.popleft()
                for neighbor in adjacency_list[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = dist + 1
                        queue.append((neighbor, dist + 1))
                        if dist + 1 > max_dist:
                            max_dist = dist + 1
                            farthest_node = neighbor
            return farthest_node, max_dist

        # Step 1: Find the depth of the tree
        # Start BFS from any node (e.g., node 0)
        first_node, _ = bfs(0)
        _, depth = bfs(first_node)

        # Step 2: Calculate degrees and find the top two highest
        degrees = [len(adjacency_list[node]) for node in range(V)]
        sorted_degrees = sorted(degrees, reverse=True)
        first_highest, second_highest = sorted_degrees[0], sorted_degrees[1]

        # Store results
        results.append((depth, first_highest, second_highest))
    
    return results


# Input Handling
test_cases = []
T = int(input())
for _ in range(T):
    V = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(V - 1)]
    test_cases.append((V, edges))

# Compute results
results = calculate_tree_properties(test_cases)

# Print results
for result in results:
    print(*result)
