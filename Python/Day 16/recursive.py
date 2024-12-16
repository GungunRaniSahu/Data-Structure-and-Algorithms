#Recursive DFS
def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")  
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

visited = set()  
print("DFS (Recursive):", end=" ")
dfs_recursive(graph, 0, visited)  
