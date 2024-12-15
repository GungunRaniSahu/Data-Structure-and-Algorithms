#BFS Implementation
from collections import deque

def bfs(graph, start_node):
    visited = set()  
  queue = deque([start_node])  
    bfs_order = []  

    while queue:
        
        current = queue.popleft()
        
        if current not in visited:
            bfs_order.append(current)
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

print("BFS Traversal:", bfs(graph, 0))  # Output: BFS Traversal: [0, 1, 2, 3, 4]
