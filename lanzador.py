from main import AplicacionScheduler

def menu():
    app = AplicacionScheduler()

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cargar procesos de ejemplo")
        print("2. Ejecutar planificación FCFS")
        print("3. Ejecutar planificación Round Robin")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            app.cargar_procesos_demo()
            print("Procesos cargados.")
        elif opcion == "2":
            if not app.procesos_cargados():
                print("No hay procesos cargados. Por favor, carga procesos antes de ejecutar un algoritmo.")
            else:
                print("Procesos disponibles para FCFS:", app.repositorio.listar_procesos())  # Depuración
                app.ejecutar_fcfs()
        elif opcion == "3":
            if not app.procesos_cargados():
                print("No hay procesos cargados. Por favor, carga procesos antes de ejecutar un algoritmo.")
            else:
                print("\nRound Robin es un algoritmo de planificación que utiliza un quantum (unidad de tiempo).")
                print("Ejemplo: Si el quantum es 4, cada proceso se ejecutará durante un máximo de 4 unidades de tiempo antes de pasar al siguiente.")
                try:
                    q = int(input("Introduce el quantum para Round Robin (ejemplo: 4): "))
                    print("Procesos disponibles para Round Robin:", app.repositorio.listar_procesos())  # Depuración
                    app.ejecutar_round_robin(q)
                except ValueError:
                    print("Quantum inválido. Debe ser un número entero.")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()