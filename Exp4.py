
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    hanoi(n - 1, auxiliary, source, destination)


n = 3
hanoi(n, 'A', 'B', 'C')




# Tower of Hanoi using State Space Search

# def hanoi(n):
#     start = (tuple(range(n, 0, -1)), (), ())
#     goal = ((), (), tuple(range(n, 0, -1)))

#     queue = [(start, [])]
#     visited = [start]

#     while queue:
#         state, path = queue.pop(0)

#         if state == goal:
#             for move in path:
#                 print(move)
#             return

#         for i in range(3):
#             if state[i]:
#                 disk = state[i][-1]

#                 for j in range(3):
#                     if i != j:
#                         if not state[j] or disk < state[j][-1]:
#                             new_state = [list(rod) for rod in state]

#                             new_state[i].pop()
#                             new_state[j].append(disk)

#                             new_state = tuple(tuple(rod) for rod in new_state)

#                             if new_state not in visited:
#                                 visited.append(new_state)

#                                 move = "Move disk " + str(disk) + \
#                                        " from " + str(i + 1) + \
#                                        " to " + str(j + 1)

#                                 queue.append((new_state, path + [move]))


# hanoi(3)

