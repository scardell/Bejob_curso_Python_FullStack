"""
La clase empleado contiene los datos que seran compartidos por su clases hijas.
La clase empleado contiene un constructor para inicializar sus atributos.
Los datos utilizados son: nombrecompleto, cedula y telefoo.
Cada atributo de la clase cuenta con sus respectivos get y set.
"""
class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono