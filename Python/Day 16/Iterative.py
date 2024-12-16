#Iterative DFS
def dfs_iterative(graph, start):
    visited = set()  
    stack = [start]  

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  
            visited.add(node)
            
            stack.extend(reversed(graph[node]))

print("\nDFS (Iterative):", end=" ")
dfs_iterative(graph, 0)  
