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
    Retorna el estado inicial del tablero
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Retorna el jugador con el siguiente turno.
    """
    countX = 0;
    countO = 0;
    # contamos el número de X y O
    for fila in board: 
        for celda in fila:
            if X == celda:
                countX += 1
            elif O == celda: 
                countO += 1
    # X siempre empieza asi que el turno de X es cuando el número de X es menor o igual que el de O
    if countX <= countO:
        return X
    else:
        return O

def actions(board):
    moves = []
    # Me puedo mover a cualquier casilla EMPTY
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
    Dime cual es el ganador, si no hay un ganador retorna None
    """
    state = None
    # Ganador horizontal
    for fila in range(len(board)): 
        state = board[fila][0] # asumo q todos los elemntos de la fila son iguales al primero
        for columna in range(len(board[fila])):
            if state != board[fila][columna]: # si no son iguales paso a la siguiente fila
                state = None
                break

        if state != None:
          return state        
    
    # Gandador vertical
    for columna in range(len(board[0])):
        state = board[0][columna] # asumo que todos los elementos de la columan son iguales al primero
        for fila in range(len(board)):
            if state != board[fila][columna]: # si no son iguales paso a la siguiente columana
                state = None
                break

        if state != None:
          return state

    # Ganador diagonal 1
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

    # Ganador diagonal 2
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
    Retorna True si el juego ha terminado y False en caso contrario
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
    Retornar 1 si X ha ganado, -1 si O ha ganado, 0 si es un empate.
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
    Retorna la acción óptima a tomar
    """
    # Si el juego ya ha terminado solo responde None
    if terminal(board):
        return None

    # Si la máquina juega con O entonces empiezo buscando el mínimo por su utilidad -1
    # Si la máguina juega con X empieza buscando el máximo por su utilidad 1
    i_am = player(board) # juego con X o O 
    new_board = cp.deepcopy(board)
    value = None
    if i_am == X:
        if new_board == [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]:
            return (1,1) # si soy X y hago el primer movimiento en el tablero me coloco en el centro.
        else:
            value = __max_value(new_board) # empiezo buscando el máximo por su utilidad 1
            for action in actions(new_board): # para cualquier acción con el mismo valor de utilidad
                if value == __min_value(result(new_board, action)):
                    return action # retorno la acción para llegar a ese estado
    else:
        value = __min_value(new_board) # empiezo buscando el mínimo por su utilidad -1
        for action in actions(new_board):
            if value == __max_value(result(new_board, action)):
                return action

def __max_value(board): 
    if terminal(board): # si el juego ha terminado retorno la utilidad del tablero
        return utility(board)
    
    value = -2 # nunca tomo valores menores a -2
    for action in actions(board):
        value = max(value, __min_value(result(board, action))) # tomo el máximo estado posible

    return value # retorno el valor máximo

def __min_value(board):
    if terminal(board): # si el juego ha terminado retorno la utilidad del tablero
        return utility(board)

    value = 2 # nunca tomo valores mayores a 2
    for action in actions(board): # para cualquier acción
        value = min(value, __max_value(result(board, action))) # tomo el mínimo estado posible

    return value # retorno el valor mínimo