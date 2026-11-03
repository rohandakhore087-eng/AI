
from heapq import heappush, heappop

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))

queue = [(heuristic(start), 0, start, [])]
visited = set()

while queue:
    f, cost, state, path = heappop(queue)

    if state == goal:
        print("Solution:")
        for s in path + [state]:
            print(s[:3], s[3:6], s[6:])
        break

    if state in visited:
        continue
    visited.add(state)

    z = state.index(0)
    for move in [-3, 3, -1, 1]:
        n = z + move

        if 0 <= n < 9 and not (move == -1 and z % 3 == 0) \
           and not (move == 1 and z % 3 == 2):
            new = list(state)
            new[z], new[n] = new[n], new[z]
            new = tuple(new)

            if new not in visited:
                heappush(queue, (cost + 1 + heuristic(new),
                                 cost + 1, new, path + [state]))
