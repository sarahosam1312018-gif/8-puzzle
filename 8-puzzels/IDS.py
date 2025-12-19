# ---------- 8 Puzzle IDS Implementation ----------

# Goal state (0 represents the blank tile)
GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

# Generate possible next states
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3

    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    for move, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append((tuple(new_state), move))

    return neighbors


# Depth-Limited DFS
def depth_limited_dfs(state, depth, visited):
    if state == GOAL_STATE:
        return []

    if depth == 0:
        return None

    visited.add(state)

    for neighbor, move in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_dfs(neighbor, depth - 1, visited)
            if result is not None:
                return [move] + result

    return None


# Iterative Deepening Search
def iterative_deepening_search(start_state, max_depth=25):
    for depth in range(max_depth + 1):
        visited = set()
        result = depth_limited_dfs(start_state, depth, visited)
        if result is not None:
            return result

    return None


# ---------- Main ----------
if __name__ == "__main__":

    #  initial state (solvable)
    start_state = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    solution = iterative_deepening_search(start_state)

    if solution:
        print("IDS Solution Found!")
        print("Moves:", solution)
        print("Number of steps:", len(solution))
    else:
        print("No solution found within the depth limit.")
