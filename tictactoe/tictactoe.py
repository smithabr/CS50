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
    countX = 0;
    countO = 0;
    for i in range(len(board)) :
        for j in range( len(board[i])) :
            if board[i][j] == X :``
                countX += 1
            if board[i][j] == O :
                countO += 1
    if countX > countO :
        return O
    else :
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset = set () 

    for i in range (len(board )):
        for j in range( len (board[i])):
            if board[i][j] == EMPTY :
                actionset.add((i,j))
    return actionset



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board) :
        raise Exception("Not a valid action")
    
    copy_board = copy.deepcopy( board )
    i,j = action
    copy_board[i][j]=player(copy_board)
    return copy_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for j in range(len(board)):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[2][j] != EMPTY :
            return board[2][j]
        if board[j][0] == board[j][1] and board[j][1] == board[j][2] and board[j][2] != EMPTY :
            return board[j][0];
            
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != EMPTY:
        return board[0][0] ;
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != EMPTY :
        return board[1][1];
    return EMPTY



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winPlayer = winner(board)
    if winPlayer == X or winPlayer == O :
        return True;
    for i in  range( len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board);
    if result == X :
        return 1
    if result == O:
        return -1
    else:
        return 0

def maxValue( board ):
    v = -math.inf
    if terminal(board):
        return utility(board )
    for action in actions(board):
        v = max( v, minValue(result(board,action)))

    return v

def minValue( board ):
    v  = math.inf
    if terminal(board):
        return utility(board )
    for action in actions(board):
        v = min( v, maxValue(result(board,action)))

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None;
    elif player(board) == X:
        plays =[]
        for action in actions (board ):
            plays.append ([minValue(result(board,action)),action])
        return sorted ( plays, key = lambda x:x[0], reverse = True )[0][1]
    elif player(board) == O:
        plays =[]
        for action in actions (board ):
            plays.append ([maxValue(result(board,action)),action])
        return sorted ( plays, key = lambda x:x[0] )[0][1]       

