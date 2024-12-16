#Detecting Cycles in an Undirected Graph
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:  
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1): 
                return True
    return False

print("\nCycle Detected:" if has_cycle(graph) else "\nNo Cycle Detected")
