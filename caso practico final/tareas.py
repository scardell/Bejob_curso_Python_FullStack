class Tarea:
    """Clase que representa una tarea."""
    def __init__(self, descripcion):
        """Inicializa una nueva tarea con una descripción y estado pendiente."""
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self):
        """Devuelve una representación en cadena de la tarea, mostrando su estado."""
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class ListaTareas:
    """Clase que gestiona una lista de tareas."""
    def __init__(self):
        """Inicializa una lista vacía de tareas."""
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista."""
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada a la lista.")

    def marcar_tarea_completada(self, posicion):
        """Marca una tarea como completada, dada su posición en la lista."""
        try:
            self.tareas[posicion].marcar_completada()
            print(f"Tarea '{self.tareas[posicion].descripcion}' marcada como completada.")
        except IndexError:
            print("Error: La posición ingresada no es válida.")

    def mostrar_tareas(self):
        """Muestra todas las tareas con su estado."""
        if not self.tareas:
            print("No hay tareas en la lista.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        """Elimina una tarea de la lista, dada su posición."""
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada de la lista.")
        except IndexError:
            print("Error: La posición ingresada no es válida.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nMenú de opciones:")
    print("1. Agregar una nueva tarea")
    print("2. Marcar una tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar una tarea")
    print("5. Salir")

def main():
    """Función principal del programa."""
    lista_tareas = ListaTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == '2':
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
                lista_tareas.marcar_tarea_completada(posicion)
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        elif opcion == '3':
            lista_tareas.mostrar_tareas()
        elif opcion == '4':
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
                lista_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
