"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return EMPTY

    flat_board = [space for sub_board in board for space in sub_board]

    X_count = flat_board.count(X)
    O_count = flat_board.count(O)

    if O_count < X_count:
        return O
    else:
        return X
    


def actions(board):
    
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    if terminal(board):
        return set(actions_set)
    for i, sub in enumerate(board):
        for j, space in enumerate(sub):
            if space is None:
                actions_set.add((i,j))
    return actions_set
                
                
                
                
                
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    who = player(board)
    if who is EMPTY:
        raise ValueError

    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = who
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        set_row = set(board[i])
        if len(set_row) == 1 and board[i][0] != EMPTY:
            return board[i][0]
    for j in range(3):
        set_column = set([board[0][j], board[1][j], board[2][j]])
        if len(set_column) == 1 and board[0][j] != EMPTY:
            return board[0][j]
    
    diag1 = set([board[0][0], board[1][1], board[2][2]])
    diag2 = set([board[0][2], board[1][1], board[2][0]])
    if (len(diag1) == 1 or len(diag2) == 1) and board[1][1] != EMPTY:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not any(EMPTY in sub for sub in board) or winner(board) is not None:
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    score = winner(board)
    if score == X:
        return 1
    elif score == O:
        return -1
    else:
        return 0

def min_value(board, alpha, beta):
    """
    Helper function for finding minimum value for minimax 
    """


    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(v, beta)
        if alpha > beta:
            break
    return v

def max_value(board, alpha, beta):

    """
    Helper function for finding maximum value for minimax 
    """

    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha > beta:
            break
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    who = player(board)
    move = set()
    if who is X:
        val = -math.inf
        for action in actions(board):
            v = min_value(result(board, action), -math.inf, math.inf)
            if v > val:
                val = v
                move = action 
    
    if who is O:
        val = math.inf
        for action in actions(board):
            v = max_value(result(board, action), -math.inf, math.inf)
            if v < val:
                val = v
                move = action
    return move
    
