
# Model-Based Agent for Grid Navigation

def move_agent(position, obstacles, visited):
    x, y = position

    moves = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]

    for new_pos in moves:
        if (0 <= new_pos[0] < 3 and
            0 <= new_pos[1] < 3 and
            new_pos not in obstacles and
            new_pos not in visited):
            return new_pos

    return position


def grid_world():
    position = (0, 0)
    goal = (2, 2)
    obstacles = [(1, 1)]
    visited = [position]

    while position != goal:
        print("Current Position:", position)

        new_position = move_agent(position, obstacles, visited)

        if new_position == position:
            print("No path found!")
            return

        position = new_position
        visited.append(position)

        print("Agent moved to:", position)

    print("Goal reached:", goal)


grid_world()
