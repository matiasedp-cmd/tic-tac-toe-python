
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


def ingresar_movimiento(tablero):
    while True:
        try:
            movimiento = int(input("Ingresa un número entero entre 1 y 9: "))
            if 1 <= movimiento <= 9:
                # 1. Calculamos fila y columna
                movimiento = movimiento - 1
                fila = movimiento // 3
                columna = movimiento % 3
                
                # 2. Revisamos si la casilla está libre (no tiene ni X ni O)
                if tablero[fila][columna] not in ['X', 'O']:
                    tablero[fila][columna] = 'O'  # Ponemos la ficha del usuario
                    break  # ¡Todo salió bien, salimos del bucle!
                else:
                    print("Celda ocupada, por favor ingrese otra.")
            else:
                print("Error: El número debe estar entre 1 y 9.")
        except ValueError:
            print("Error: Eso no es un número entero. Inténtalo de nuevo.")



