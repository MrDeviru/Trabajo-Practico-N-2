def cargar_matriz(jugadores):
    for i in range(len(jugadores)):
        nombre = input(f"Ingrese el nombre del jugador {i + 1}: ")
        apellido = input(f"Ingrese el apellido del jugador {i + 1}: ")
        posicion = input(f"Ingrese la posición del jugador {i + 1}: ")
        edad = input(f"Ingrese la edad del jugador {i + 1}: ")
        goles = input(f"Ingrese los goles del jugador {i + 1}: ")
        jugadores[i] = [nombre, apellido, posicion, edad, goles]

def mostrar_matriz(jugadores):
    print("NOMBRE | APELLIDO | POSICIÓN | EDAD | GOLES")
    for fila in jugadores:
        print(" | ".join(str(dato) for dato in fila))

def modificar_matriz(jugadores):
    mostrar_matriz(jugadores)
    fila = int(input("Ingrese la fila del jugador a modificar (0-10): "))
    columna = int(input("Ingrese la columna a modificar (0:Nombre, 1:Apellido, 2:Posición, 3:Edad, 4:Goles): "))
    nuevo_dato = input("Ingrese el nuevo dato: ")
    jugadores[fila][columna] = nuevo_dato
    print("Dato modificado correctamente.")

