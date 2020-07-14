"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    x_count = 0
    o_count = 0
    empty_count = 0
    for i in board :
        for j in i:
            if j==X :
                x_count+=1
            elif j==O :
                o_count+=1
            else :
                empty_count+=1
    if x_count > o_count :
        return O
    else :
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(0,3) :
        for j in range(0,3):
            if board[i][j]==EMPTY :
                actions_set.add((i,j))
    return actions_set   
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    if board[i][j]==EMPTY :
        final_board = copy.deepcopy(board)
        final_board[i][j] = player(board)
        return final_board
    else :
        raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0]==board[1][1]==board[2][2]!=EMPTY) :
        return board[0][0]
    elif (board[0][0]==board[0][1]==board[0][2]!=EMPTY) :
        return board[0][0]
    elif (board[1][0]==board[1][1]==board[1][2]!=EMPTY) :
        return board[1][0]
    elif (board[2][0]==board[2][1]==board[2][2]!=EMPTY) :
        return board[2][0]
    elif (board[0][2]==board[1][1]==board[2][0]!=EMPTY) :
        return board[0][2]
    elif (board[0][0]==board[1][0]==board[2][0]!=EMPTY) :
        return board[0][0]
    elif (board[0][1]==board[1][1]==board[2][1]!=EMPTY) :
        return board[1][1]
    elif (board[0][2]==board[1][2]==board[2][2]!=EMPTY) :
        return board[2][2]
    else :
        return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None :
        for i in board :
            for j in i:
                if j==EMPTY :
                    return False
        return True
    else :
        return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    var = winner(board)
    if var is None:
        return 0
    elif var==X :
        return 1
    else :
        return -1

tup = ()
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else :
        global tup
        tup = ()
        i = minimax_sub(board)
        return tup

    # raise NotImplementedError
def minimax_sub(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    else :
        player_turn = player(board)
        s = actions(board)
        global tup
        if len(s)==9 :
            tup = (random.randint(0, 2),random.randint(0, 2))
            return 0
        if player_turn == X :
            val = -2
            values = {}
            for x in s :
                val = max(val,minimax_sub(result(board,x)))
                values[x] =val 
                if val==1 :
                    tup = x
                    return 1
            for x in values.keys() :
                if values[x]==0 :
                    tup = x
                    return 0
            for x in values.keys() :
                if values[x]==-1 :
                    tup = x
                    return -1
        else :
            val = 2
            values = {}
            for x in s :
                val = min(val,minimax_sub(result(board,x)))
                values[x] =val
                if val==-1 :
                    tup = x
                    return -1
            for x in values.keys() :
                if values[x]==0 :
                    tup = x
                    return 0
            for x in values.keys() :
                if values[x]==1 :
                    tup = x
                    return 1