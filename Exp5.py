
from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            print("Path:", path)
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])

    print("Path not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A', 'F')
