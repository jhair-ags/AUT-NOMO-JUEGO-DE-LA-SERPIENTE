#  Snake Game - Versión Consola en Python

##  Descripción

Este proyecto es una versión del clásico juego Snake, desarrollada en Python y ejecutada en consola.

Actualmente el programa incluye un menú interactivo, sistema de juego completo y opción para visualizar el puntaje obtenido.

El objetivo del juego es controlar la serpiente, comer la comida representada por un símbolo y crecer sin chocar contra los bordes del tablero ni contra su propio cuerpo.

El proyecto fue desarrollado utilizando estructuras básicas de programación como:

- Variables  
- Condicionales (if)  
- Ciclos (while, for)  
- Listas  
- Funciones  
- Entrada de datos con input()  
- Generación de números aleatorios con random  

---

##  Estructura del Programa

El programa está dividido en las siguientes partes:

- Menú principal
- Función jugar()
- Función mostrar_reglas()
- Sistema de movimiento
- Sistema de colisiones
- Sistema de puntaje
- Generación aleatoria de comida

---

##  Cómo funciona el juego

- El tablero es una cuadrícula de 10x10.
- La serpiente inicia en el centro del tablero.
- La comida aparece en posiciones aleatorias.
- El jugador controla la serpiente con el teclado.
- El menú permite navegar entre opciones antes de iniciar el juego.

###  Opciones del menú

1. Jugar  
2. Ver reglas  
3. Ver puntaje  
4. Salir  

---

##  Controles

W → Arriba  
S → Abajo  
A → Izquierda  
D → Derecha  

---

##  Lógica del programa

El programa funciona de la siguiente manera:

1. Se solicitan datos al usuario (nombre y edad).
2. Se muestra el menú principal.
3. Si el jugador elige jugar:
   - Se inicializa el tablero.
   - Se crea la serpiente como lista de coordenadas.
   - Se genera comida en una posición aleatoria.
4. Se dibuja el tablero en consola usando símbolos:
   O → cabeza  
   o → cuerpo  
   * → comida  
   . → espacio vacío  
5. Se ejecuta un ciclo principal que:
   - Dibuja el tablero.
   - Pide movimiento al jugador.
   - Actualiza la posición.
   - Verifica colisiones.
   - Detecta si la serpiente come comida.
6. El juego termina cuando la serpiente:
   - Choca contra una pared.
   - Choca contra sí misma.
7. El sistema muestra el puntaje final y permite regresar al menú.

---

##  Requisitos

- Python 3.x instalado.
- No requiere librerías externas (solo se utiliza random, incluida en Python).

---

##  Cómo ejecutar el juego

1. Guardar el código en un archivo llamado:

   snake.py

2. Abrir una terminal o consola en la carpeta del archivo.
3. Ejecutar el siguiente comando:

   python snake.py

4. Seleccionar una opción del menú y comenzar a jugar.

---

##  Posibles mejoras futuras

- Aumentar dificultad progresiva.
- Mejorar diseño visual.
- Crear versión gráfica.
- Guardar puntuación máxima en archivo.
- Implementar niveles.

---

##  Aprendizajes obtenidos

Durante el desarrollo del proyecto se reforzaron conceptos como:

- Manejo de listas para representar el cuerpo de la serpiente.
- Uso de ciclos para crear el bucle principal del juego.
- Condicionales para validar colisiones y eventos.
- Generación de números aleatorios.
- Organización del código en funciones.
- Creación de menús interactivos.
- Resolución de problemas investigando documentación adicional.

---

##  Autor
Jhair G.
