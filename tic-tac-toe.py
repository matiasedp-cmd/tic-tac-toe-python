
tablero = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
]

def mostrar_tablero(tablero):
    for fila in range(len(tablero)):
        print('+-------+-------+-------+')
        print('|', '|', '|', '|', sep='       ')
        print('|   ', tablero[fila][0], '   |   ', tablero[fila][1], '   |   ', tablero[fila][2], '   |', sep='')
        print('|', '|', '|', '|', sep='       ')
    print('+-------+-------+-------+')

mostrar_tablero(tablero)