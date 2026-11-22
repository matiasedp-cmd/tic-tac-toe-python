from random import randrange

tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]


def mostrar_tablero(tablero):
    for fila in range(len(tablero)):
        print("+-------+-------+-------+")
        print("|", "|", "|", "|", sep="       ")
        print(
            "|   ",
            tablero[fila][0],
            "   |   ",
            tablero[fila][1],
            "   |   ",
            tablero[fila][2],
            "   |",
            sep="",
        )
        print("|", "|", "|", "|", sep="       ")
    print("+-------+-------+-------+")


def ingresar_movimiento(tablero):
    while True:
        try:
            movimiento = int(input("Casilla: "))
            if 1 <= movimiento <= 9:
                # 1. Calculamos fila y columna
                movimiento = movimiento - 1
                fila = movimiento // 3
                columna = movimiento % 3

                # 2. Revisamos si la casilla está libre (no tiene ni X ni O)
                if tablero[fila][columna] not in ["X", "O"]:
                    tablero[fila][columna] = "O"  # Ponemos la ficha del usuario
                    break  # ¡Todo salió bien, salimos del bucle!
                else:
                    print("Celda ocupada, por favor ingrese otra.")
            else:
                print("Error: El número debe estar entre 1 y 9.")
        except ValueError:
            print("Error: Eso no es un número entero. Inténtalo de nuevo.")


def listar_campos_libres(tablero):
    libres = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] not in ["X", "O"]:
                libres.append((fila, columna))
    return libres


def victoria_para(tablero, signo):
    for i in range(3):
        # Revisa filas
        if tablero[i][0] == signo and tablero[i][1] == signo and tablero[i][2] == signo:
            return True
        # Revisa columnas
        if tablero[0][i] == signo and tablero[1][i] == signo and tablero[2][i] == signo:
            return True
    # Revisa diagonales
    if tablero[0][0] == signo and tablero[1][1] == signo and tablero[2][2] == signo:
        return True
    return bool(
        tablero[0][2] == signo and tablero[1][1] == signo and tablero[2][0] == signo
    )


def dibujar_movimiento(tablero):
    libres = listar_campos_libres(tablero)
    cantidad = len(libres)
    if cantidad > 0:
        indice = randrange(cantidad)
        fila, columna = libres[indice]
        tablero[fila][columna] = "X"


def jugar():
    tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    turno_usuario = True

    while len(listar_campos_libres(tablero)) > 0:
        mostrar_tablero(tablero)
        if turno_usuario:
            ingresar_movimiento(tablero)
            if victoria_para(tablero, "O"):
                mostrar_tablero(tablero)
                print("¡Has ganado!")
                return
        else:
            dibujar_movimiento(tablero)
            if victoria_para(tablero, "X"):
                mostrar_tablero(tablero)
                print("¡La máquina ha ganado!")
                return
        turno_usuario = not turno_usuario

    mostrar_tablero(tablero)
    print("¡Empate!")


# --- Ejecución principal ---
print("Bienvenido a Tic-Tac-Toe. Elige una casilla libre (1-9) para jugar.\n")

while True:
    jugar()
    while True:
        opcion = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()
        if opcion in ["s", "si", "sí", "n", "no"]:
            break
        print("Respuesta inválida. Escribe 's' para sí o 'n' para no.")

    if opcion in ["n", "no"]:
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    print("\n--- Nueva partida ---\n")