#Topological Sorting with DFS (for Directed Acyclic Graphs)
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  

dag = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}

print("\nTopological Sort:", topological_sort(dag))
