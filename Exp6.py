
def dfs(graph, node, goal, visited):
    if node == goal:
        print("Goal found:", node)
        return True

    visited.append(node)
    print("Visiting:", node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):
                return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A', 'F', [])
