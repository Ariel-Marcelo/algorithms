"""
Tic Tac Toe Player
"""
import math
import copy as cp
# Posibles movimientos
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
    for fila in board: 
        for celda in fila:
            if X == celda:
                countX += 1
            elif O == celda: 
                countO += 1
    
    if countX <= countO:
        return X
    else:
        return O

def actions(board):
    moves = []
    for fila in range(len(board)): 
        for columna in range(len(board[fila])):
            if board[fila][columna] == EMPTY:
                moves.append((fila,columna))
    
    return moves
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    new_board = cp.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    state = None
    # Check horizontal
    for fila in range(len(board)): 
        state = board[fila][0]
        for columna in range(len(board[fila])):
            if state != board[fila][columna]:
                state = None
                break

        if state != None:
          return state        
    
    # Check vertical
    for columna in range(len(board[0])):
        state = board[0][columna]
        for fila in range(len(board)):
            if state != board[fila][columna]:
                state = None
                break

        if state != None:
          return state

    # Check diagonal 1
    acumulador = 0
    state = board[0][0]
    for fila in range(len(board)):
        if state != board[fila][acumulador]:
            state = None
            acumulador = 0
            break              
        
        acumulador += 1

    if state != None:
      return state

    # Check diagonal 2
    state = board[len(board) - 1][0]
    acumulador = len(board[0]) - 1
    for fila in range(len(board)):
        if state != board[fila][acumulador]:
            state = None
            acumulador = 0
            break              
        
        acumulador -= 1

    return state


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        if actions(board) == []:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Si el juego ya ha terminado solo responde None
    if terminal(board):
        return None

    # Si la máquina juega con O entonces empiezo buscando el mínimo 
    # Si la máguina juega con X empieza buscando el máximo
    i_am = player(board)
    new_board = cp.deepcopy(board)
    value = None
    if i_am == X:
        if new_board == [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]:
            return (1,1)
        else:
            value = __max_value(new_board)
            for action in actions(new_board):
                if value == __min_value(result(new_board, action)):
                    return action
    else:
        value = __min_value(new_board)
        for action in actions(new_board):
            if value == __max_value(result(new_board, action)):
                return action

def __max_value(board): 
    if terminal(board):
        return utility(board)
    
    value = -2
    for action in actions(board):
        value = max(value, __min_value(result(board, action)))

    return value

def __min_value(board):
    if terminal(board):
        return utility(board)

    value = 2
    for action in actions(board):
        value = min(value, __max_value(result(board, action)))

    return value