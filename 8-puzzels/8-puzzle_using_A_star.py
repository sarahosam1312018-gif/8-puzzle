import heapq
import itertools

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


class PuzzleState:
    def __init__(self, board, cost=0, path=None):
        self.board = board
        self.cost = cost            
        self.h = manhattan_distance(board)
        self.f = self.cost + self.h # function 
        self.path = path if path is not None else [board]
        self.key = self._board_to_tuple(board)

    def _board_to_tuple(self, board):
        return tuple(tuple(row) for row in board)

    def is_goal(self):
        return self.board == GOAL_STATE

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.get_blank_position()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

                successors.append(
                    PuzzleState(
                        new_board,
                        self.cost + 1,
                        self.path + [new_board]
                    )
                )
        return successors


def print_board(board):
    for row in board:
        print(row)
    print()


def a_star_search(initial_board):
    initial_state = PuzzleState(initial_board)

    frontier = []
    counter = itertools.count()
    heapq.heappush(frontier, (initial_state.f, next(counter), initial_state))

    explored = set()

    while frontier:
        _, _, state = heapq.heappop(frontier)

        if state.is_goal():
            return state.path, state.cost

        if state.key in explored:
            continue

        explored.add(state.key)

        for successor in state.generate_successors():
            if successor.key not in explored:
                heapq.heappush(
                    frontier,
                    (successor.f, next(counter), successor)
                )

    return None, None


if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    path, cost = a_star_search(initial_board)

    if path:
        print("Solution found using A* with Manhattan Distance.")
        print("Number of moves:", cost)
        print("Steps:\n")

        for step, board in enumerate(path):
            print(f"Step {step}:")
            print_board(board)
    else:
        print("No solution exists.")
