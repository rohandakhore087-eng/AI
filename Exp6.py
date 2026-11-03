def dfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    stack = [(start, [start])]
    visited = [start]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while stack:
        current, path = stack.pop()

        if current == goal:
            print("Path:", path)
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
                stack.append((next_pos, path + [next_pos]))

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

dfs(grid, start, goal)