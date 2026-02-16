import random  # Importa la librería para generar números aleatorios

# Tamaño del tablero
ancho = 10
alto = 10

# Posición inicial de la serpiente (lista de coordenadas)
snake = [(5,5)]

# Dirección inicial (derecha)
direccion = "d"

# Posición inicial de la comida en lugar aleatorio
comida = (random.randint(0, ancho-1), random.randint(0, alto-1))


# Función para dibujar el tablero en consola
def dibujar():
    for y in range(alto):  # Recorre filas
        fila = ""
        for x in range(ancho):  # Recorre columnas
            if (x,y) == snake[0]:
                fila += "O"  # Cabeza de la serpiente
            elif (x,y) in snake:
                fila += "o"  # Cuerpo de la serpiente
            elif (x,y) == comida:
                fila += "*"  # Comida
            else:
                fila += "."  # Espacio vacío
        print(fila)


# Bucle principal del juego
while True:
    dibujar()  # Muestra tablero

    # Pide movimiento al jugador
    move = input("Mover (w/a/s/d): ").lower()

    # Si el movimiento es válido cambia dirección
    if move in ["w","a","s","d"]:
        direccion = move

    # Obtiene posición actual de la cabeza
    x,y = snake[0]

    # Cambia coordenadas según dirección
    if direccion == "w": y -= 1  # Arriba
    if direccion == "s": y += 1  # Abajo
    if direccion == "a": x -= 1  # Izquierda
    if direccion == "d": x += 1  # Derecha

    nueva = (x,y)  # Nueva posición cabeza

    # Detecta colisiones (pared o cuerpo)
    if x<0 or x>=ancho or y<0 or y>=alto or nueva in snake:
        print("Game Over ")
        break

    # Agrega nueva cabeza
    snake.insert(0, nueva)

    # Si come comida crece, si no elimina cola
    if nueva == comida:
        comida = (random.randint(0, ancho-1), random.randint(0, alto-1))
    else:
        snake.pop()  # Quita último segmento