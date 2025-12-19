
from collections import deque

GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


def get_blank_index(state):
    return state.index(0)


def swap_positions(state, i, j):
    temp = list(state)
    temp[i], temp[j] = temp[j], temp[i]
    return tuple(temp)


def get_neighbors(state):
    neighbors = []
    blank = get_blank_index(state)

    row = blank // 3
    col = blank % 3

    if row > 0:
        neighbors.append(("Up", swap_positions(state, blank, blank - 3)))
    if row < 2:
        neighbors.append(("Down", swap_positions(state, blank, blank + 3)))
    if col > 0:
        neighbors.append(("Left", swap_positions(state, blank, blank - 1)))
    if col < 2:
        neighbors.append(("Right", swap_positions(state, blank, blank + 1)))

    return neighbors


def bfs(start_state):
    queue = deque([start_state])
    parent = {start_state: None}
    action = {start_state: None}

    while queue:
        current = queue.popleft()

        if current == GOAL_STATE:
            return build_path(parent, action, current)

        for move, next_state in get_neighbors(current):
            if next_state not in parent:
                parent[next_state] = current
                action[next_state] = move
                queue.append(next_state)

    return None


def build_path(parent, action, state):
    path = []
    while parent[state] is not None:
        path.append(action[state])
        state = parent[state]
    path.reverse()
    return path


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# -------- Main --------
if __name__ == "__main__":

    start_state = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    solution = bfs(start_state)

    if solution:
        print("BFS Solution Found")
        print("Moves:", solution)
        print("Number of moves:", len(solution))
    else:
        print("No solution found")
