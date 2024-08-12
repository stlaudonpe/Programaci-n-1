tablero = [[0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

jugador_actual = 1
ultimo_numero = 0  
# Comienza en 0, para que el primer jugador coloque el número 1
ultima_posicion = (-1, -1)  
# Guardamos la última posición jugada (fila, columna)

def imprimir_tablero(tablero):
    print("Este es el tablero actual: ")
    tablero_cadena = ""
    for fila in tablero:
        for celda in fila:
            tablero_cadena = tablero_cadena + str(celda)
            tablero_cadena = tablero_cadena + " "
        tablero_cadena = tablero_cadena + "\n"
    print(tablero_cadena)

def imprimir_instrucciones():
    print(
        """
----------------------------------------------------------------------------------------------------------------------------------------------------------        
Bienvenido a Numbo.
    El primer jugador introduce el número '1' en cualquier cuadrado.
    El segundo jugador escribe '2' en cualquier lugar de la misma fila o columna, de manera consecutiva por turnos. 
    Cada nuevo número debe colocarse en un movimiento de torre no interrumpido que se aleje de su predecesor.  
    El juego continúa hasta que un jugador pierde por no tener movimiento legal. 
    El ganador anota el valor del último número introducido. Un jugador que prevé la derrota puede abandonar, disminuyendo así la puntuación del ganador.
----------------------------------------------------------------------------------------------------------------------------------------------------------
        """
    )

def jugada_legal(tablero, fila, columna, ultimo_numero, ultima_posicion):
    if tablero[fila][columna] != 0:
        return False  
    # La celda ya está ocupada
    
    # Si es el primer movimiento
    if ultimo_numero == 0:  
        # Cambiado de 1 a 0
        return True
    
    # Movimiento en la misma fila o columna
    if fila == ultima_posicion[0] or columna == ultima_posicion[1]:
        # Movimiento de torre no interrumpido (no puede saltar casillas ocupadas)
        if fila == ultima_posicion[0]:  # Misma fila
            min_col, max_col = sorted([columna, ultima_posicion[1]])
            for c in range(min_col + 1, max_col):
                if tablero[fila][c] != 0:
                    return False
                #sorted([columna, ultima_posicion[1]]): Ordena la columna actual y la columna de la última posición jugada.
        elif columna == ultima_posicion[1]:  # Misma columna
            min_fila, max_fila = sorted([fila, ultima_posicion[0]])
            for r in range(min_fila + 1, max_fila):
                if tablero[r][columna] != 0:
                    return False
        return True
    return False

def juego_terminado(tablero, ultimo_numero, ultima_posicion):
    for fila in range(6):
        for columna in range(6):
            if jugada_legal(tablero, fila, columna, ultimo_numero, ultima_posicion):
                return False  
            # Todavía hay un movimiento legal
    return True  
# No quedan movimientos legales

def jugar_numbo():
    global jugador_actual, ultimo_numero, ultima_posicion
    #global se estan modificando las variables de manera global
    imprimir_instrucciones()
    imprimir_tablero(tablero)
    
    while not juego_terminado(tablero, ultimo_numero, ultima_posicion):
        try:
            print(f"Turno del jugador {jugador_actual}, introduzca el número {ultimo_numero + 1}")
            ingreso_fila = int(input("Ingrese la fila (1-6): ")) - 1
            ingreso_columna = int(input("Ingrese la columna (1-6): ")) - 1
            
            if jugada_legal(tablero, ingreso_fila, ingreso_columna, ultimo_numero, ultima_posicion):
                ultimo_numero += 1
                tablero[ingreso_fila][ingreso_columna] = ultimo_numero
                ultima_posicion = (ingreso_fila, ingreso_columna)
                imprimir_tablero(tablero)
                jugador_actual = 1 if jugador_actual == 2 else 2  # Cambia de jugador
            else:
                print("Movimiento ilegal, intente nuevamente.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")
    
    print(f"El juego ha terminado. Ganador: Jugador {1 if jugador_actual == 2 else 2} con una puntuación de {ultimo_numero}.")

# Iniciar el juego
jugar_numbo()
