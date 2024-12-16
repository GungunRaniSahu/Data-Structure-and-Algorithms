#Finding Connected Components with DFS
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    5: [6, 7],
    6: [5],
    7: [5]
}

def dfs_components(graph):
    visited = set()
    components = []

    def dfs(node):
        component = []
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.append(current)
                stack.extend(graph[current])
        return component

    for node in graph:
        if node not in visited:
            components.append(dfs(node))
    return components

print("\nConnected Components:", dfs_components(graph))
