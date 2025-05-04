from funciones import cargar_matriz, mostrar_matriz, modificar_matriz

def main():
    jugadores = [["" for _ in range(5)] for _ in range(11)]

    while True:
        print("\nMenú:")
        print("1. Cargar datos de los jugadores")
        print("2. Mostrar matriz")
        print("3. Modificar un dato")
        print("4. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            cargar_matriz(jugadores)
        elif opcion == "2":
            mostrar_matriz(jugadores)
        elif opcion == "3":
            modificar_matriz(jugadores)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
