class Tarea:
    # Clase que representa una tarea.
    def __init__(self, descripcion):
        # Inicializa una nueva tarea con una descripción y estado pendiente.
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        # Marca la tarea como completada.
        self.completada = True

    def __str__(self):
        # Devuelve una representación en cadena de la tarea, mostrando su estado.
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class ListaTareas:
    # Clase que gestiona una lista de tareas.
    def __init__(self):
        # Inicializa una lista vacía de tareas.
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # Agrega una nueva tarea a la lista.
        self.tareas.append(Tarea(descripcion))
        print(f"Tarea '{descripcion}' agregada a la lista.")

    def marcar_tarea_completada(self, posicion):
        # Marca una tarea como completada, dada su posición en la lista.
        if 0 <= posicion < len(self.tareas):
            self.tareas[posicion].marcar_completada()
            print(f"Tarea '{self.tareas[posicion].descripcion}' marcada como completada.")
        else:
            raise IndexError("La posicion introducida no es valida.")

    def mostrar_tareas(self):
        # Muestra todas las tareas con su estado.
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        # Elimina una tarea de la lista, dada su posición.
        if 0 <= posicion < len(self.tareas):
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada de la lista.")
        else:
            raise IndexError("La posicion ingresada no es valida.")

def mostrar_menu():
    # Muestra el menú de opciones al usuario.
    print("\nMenu de opciones:")
    print("1. Agregar una nueva tarea")
    print("2. Marcar una tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar una tarea")
    print("5. Salir")

def main():
    # Función principal del programa.
    lista_tareas = ListaTareas()

    while True:
        mostrar_menu()
        opcion = input("Introduzca el numero de la opcion deseada: ")

        try:
            if opcion == '1':
                descripcion = input("Introduzca la descripcion de la nueva tarea: ")
                lista_tareas.agregar_tarea(descripcion)
            elif opcion == '2':
                if not lista_tareas.tareas:
                    print("No hay tareas para marcar como completadas.")
                else:
                    lista_tareas.mostrar_tareas()
                    posicion = int(input("Introduzca la posicion de la tarea a marcar como completada: ")) - 1
                    lista_tareas.marcar_tarea_completada(posicion)
            elif opcion == '3':
                lista_tareas.mostrar_tareas()
            elif opcion == '4':
                if not lista_tareas.tareas:
                    print("No hay tareas para eliminar.")
                else:
                    lista_tareas.mostrar_tareas()
                    posicion = int(input("Introduzca la posicion de la tarea a eliminar: ")) - 1
                    lista_tareas.eliminar_tarea(posicion)
            elif opcion == '5':
                print("Saliendo del programa.")
                break
            else:
                print("Opcion no valida. Por favor, seleccione una opcion del 1 al 5.")
        except ValueError:
            print("Error: Debe introducir un numero valido.")
        except IndexError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
