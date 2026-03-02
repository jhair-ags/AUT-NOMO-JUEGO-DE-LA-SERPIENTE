import random

# Tamaño del tablero
ANCHO = 10
ALTO = 10

# Puntuación máxima global
max_puntos = 0


# -------- FUNCION REGLAS --------
def mostrar_reglas():
    print("\n=== REGLAS DEL JUEGO ===")
    print("Usa W A S D para mover la serpiente.")
    print("O = cabeza")
    print("o = cuerpo")
    print("* = comida")
    print("No choques con paredes ni contigo mismo.")
    print("========================\n")


# -------- FUNCION JUEGO --------
def jugar(nombre):
    global max_puntos

    snake = [(5, 5)]
    direccion = "d"
    puntos = 0

    comida = (random.randint(0, ANCHO - 1),
              random.randint(0, ALTO - 1))

    # Dibujar tablero
    def dibujar():
        for y in range(ALTO):
            fila = ""
            for x in range(ANCHO):
                if (x, y) == snake[0]:
                    fila += "O"
                elif (x, y) in snake:
                    fila += "o"
                elif (x, y) == comida:
                    fila += "*"
                else:
                    fila += "."
            print(fila)

    # Bucle del juego
    while True:
        print("\nJugador:", nombre)
        print("Puntos:", puntos)
        dibujar()

        move = input("Mover (w/a/s/d): ").lower()

        if move in ["w", "a", "s", "d"]:
            direccion = move

        x, y = snake[0]

        # Movimiento
        if direccion == "w":
            y -= 1
        elif direccion == "s":
            y += 1
        elif direccion == "a":
            x -= 1
        elif direccion == "d":
            x += 1

        nueva = (x, y)

        # Colisión
        if x < 0 or x >= ANCHO or y < 0 or y >= ALTO or nueva in snake:
            print("\n GAME OVER")
            print("Puntaje final:", puntos)

            if puntos > max_puntos:
                max_puntos = puntos
                print("Nueva puntuación máxima!")

            break

        snake.insert(0, nueva)

        # Comer comida
        if nueva == comida:
            puntos += 1
            comida = (random.randint(0, ANCHO - 1),
                      random.randint(0, ALTO - 1))
        else:
            snake.pop()


# -------- MENU PRINCIPAL --------
print("=== BIENVENIDO AL SNAKE PYTHON ===")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

while True:
    print("\nHola", nombre, "(", edad, "años )")
    print("1. Jugar")
    print("2. Ver reglas")
    print("3. Ver puntuación máxima")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        jugar(nombre)
    elif opcion == "2":
        mostrar_reglas()
    elif opcion == "3":
        print("Puntuación máxima:", max_puntos)
    elif opcion == "4":
        print("Gracias por jugar ")
        break
    else:
        print("Opción inválida")