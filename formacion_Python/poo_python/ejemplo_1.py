"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredaran de la clase Padre Vehiculo.
la clase Padre debe tener los siguientes atributos y metodos

Vehiculo (Clase Padre):
-Atributos (color , ruedas)
-Metodos ( __init__ , __str__ )

Coche (Clase Hija de Vehiculo) (Ademas de los atributos y metodos heredados de Vehiculo):
-Atributos (velocidad (km/hr))
-Metodos ( __init__ , __str__ )

Bicicleta (Clase Hija de Vehiculo) (Ademas de los atributos y metodos heredados de Vehiculo):
-Atributos (tipo (urbana/montaña/etc))
-Metodos ( __init__ , __str__ )
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: '+ str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color,ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad (km/hr): ' + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo' + self.tipo

# Creamos un objeto de la clase Vehiculo
vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

# Creamos un objeto de la clase hija Coche
coche = Coche('Azul', 4, 150)
print(coche)

# Creamos un objeto de la clase hija Bicicleta
bicicleta = Bicicleta('Blanca', 2, 'Urbano')
print(bicicleta)