from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start, [start])])
    visited = [start]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        current, path = queue.popleft()

        if current == goal:
            print("Shortest Path:", path)
            print("Total Moves:", len(path) - 1)
            return

        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            next_pos = (nr, nc)

            if (0 <= nr < rows and 0 <= nc < cols
                and grid[nr][nc] != '#'
                and next_pos not in visited):

                visited.append(next_pos)
                queue.append((next_pos, path + [next_pos]))

    print("Goal Not Reached")


grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (4, 4)

bfs(grid, start, goal)