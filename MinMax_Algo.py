import copy

"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count, o_count = 0, 0
    # loops over all the cells and counts the occurrences
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    # if x has less occurrences, or the board is empty, it is X's turn
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board)):
            value = board[i][j]
            if value == EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if the move is invalid, raise an exception
    if action not in actions(board):
        raise ValueError("Move invalid")

    copied_board = copy.deepcopy(board)  # deep copy of the board
    (i, j) = action
    copied_board[i][j] = player(board)  # update the board copy with the new action move
    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for a horizontal win
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    # check for a vertical win
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    # check for a diagonal win
    if (board[0][0] == board[1][1] == board[2][2]) or (
        board[2][0] == board[1][1] == board[0][2]
    ):
        return board[1][1]
    # else if the game has no winner
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # returns True if there is a winner or no actions are left
    return winner(board) != None or not actions(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ = winner(board)
    if champ == X:
        return 1
    elif champ == O:
        return -1
    else:
        return 0


def minimax(board):
    
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board)==X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

def max_value(board):
    """
    Helper method for finding maximum utility of a board
    """
    if terminal(board):
        return utility(board),None
    vmax=float('-inf')
    optimal_action=None
    for action in actions(board):
        min_utility=min_value(result(board,action))[0]
        if min_utility>vmax:
            vmax=min_utility
            optimal_action=action
    return vmax,optimal_action


def min_value(board):
    """
    Helper method for finding minimum utility of a board
    """
    if terminal(board):
        return utility(board),None
    vmin=float('inf')
    optimal_action=None
    for action in actions(board):
        max_utility=max_value(result(board,action))[0]
        if max_utility<vmin:
            vmin=max_utility
            optimal_action=action
    return vmin,optimal_action



def print_board(board):
    """Displays the current board state"""
    symbols = {None: " ", "X": "X", "O": "O"}
    for row in board:
        print("|".join(symbols[cell] for cell in row))


def main():
    board = initial_state()
    print_board(board)

    while True:
        # Human's turn
        while True:
            try:
                row = int(input("Human player, select a row (1-3): ")) - 1
                col = int(input("Human player, select a column (1-3): ")) - 1
                action = (row, col)
                if action in actions(board):
                    board = result(board, action)
                    print_board(board)
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter integers.")

        if terminal(board):
            break

        # AI's turn
        print("AI's turn...")
        ai_move = minimax(board)
        board = result(board, ai_move)
        print_board(board)

        if terminal(board):
            break

    the_winner = winner(board)
    if the_winner is not None:
        print(f"The winner is: {the_winner}!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
