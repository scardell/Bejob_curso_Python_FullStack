"""
La clase empleado contiene los datos que seran compartidos por su clases hijas.
La clase empleado contiene un constructor para inicializar sus atributos.
Los datos utilizados son: nombrecompleto, cedula y telefoo.
Cada atributo de la clase cuenta con sus respectivos get y set.
"""
class Empleado:
	def __init__(self, nombre, cedula, telefono):
		self._nombre = nombre
		self._cedula = cedula
		self._telefono = telefono

	def set_nombre(self, nombre):
		self._nombre = nombre
	
	def get_nombre(self):
		return self._nombre
	
	def set_cedula(self, cedula):
		self._cedula = cedula
	
	def get_cedula(self):
		return self._cedula
	
	def set_telefono(self, telefono):
		self._telefono = telefono

	def get_telefono(self):
		return self._telefono

"""
Añadimos la clase Empleado por tiempo definido que hereda de la clase Empleado.
Los nuevos atributos son; Numero de plaza, Salario, Duracion de contrato en meses.
Ademas, cuenta con n metodo que calcula el salrio total.
El empleado recibe un aumento del 2% sobre su salario base.
"""

class EmpleadoDefinido(Empleado):
	def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, duracion_contrato):
		#constructor de la clase empleado
		super().__init__(nombre, cedula, telefono)

		#Nuevos atributos
		self._nPlaza = nPlaza
		self._salarioBase = salarioBase
		self._duracion_contrato = duracion_contrato
	
	def set_nPlaza(self, nPlaza):
		self._nPlaza = nPlaza

	def get_nPlaza(self):
		return self._nPlaza
	
	def set_salarioBase(self, salarioBase):
		self._salarioBase = salarioBase
	
	def get_salarioBase(self):
		return self._salarioBase
	
	def set_duracion_contrato(self, duracion_contrato):
		self._duracion_contrato = duracion_contrato

	def get_duracion_contrato(self):
		return self._duracion_contrato
	
	#calcular salario total
	def calcularSalarioTotal(self):
		return self._salarioBase + (self._salarioBase * 0.02)
	
"""
Añadimos la clase EmpleadoIndefinido que hereda de la clase empleado.
Los nuevos atributos son; Numero de plaza, Salario base y categoria (1,2,3).
ademas, cuenta con un metodo que calcula el salario total en funcion de su categoria.
Categoria 1 . 3%
Categoria 2 . 5%
Categoria 3 . 8%
"""
class EmpleadoIndefinido(Empleado):
	def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, categoria):
		#constructor de la clase empleado
		super().__init__(nombre, cedula, telefono)

		#Nuevos atributos
		self._nPlaza = nPlaza
		self._salarioBase = salarioBase
		self._categoria = categoria
	
	def set_nPlaza(self, nPlaza):
		self._nPlaza = nPlaza

	def get_nPlaza(self):
		return self._nPlaza
	
	def set_salarioBase(self, salarioBase):
		self._salarioBase = salarioBase
	
	def get_salarioBase(self):
		return self._salarioBase
	
	def set_categoria(self, categoria):
		self._categoria = categoria

	def get_categoria(self):
		return self._categoria
	
	#calcular salario total
	def calcularSalarioTotal(self):
		if self._categoria == 1:
			return self._salarioBase + (self._salarioBase * 0.03)
		elif self._categoria == 2:
			return self._salarioBase + (self._salarioBase * 0.05)
		elif self._categoria == 3:
			return self._salarioBase + (self._salarioBase * 0.08)
		else:
			return self._salarioBase

"""
Añadimos la clase Empleado subcontratado que hereda de la clase empleado.
El nuevo atributo es empresa responsable.
"""
class EmpleadoSubcontratado(Empleado):
	def __init__(self, nombre, cedula, telefono, empresaResponsable):
		#constructor de la clase empleado
		super().__init__(nombre, cedula, telefono)

		#Nuevo atributo
		self._empresaResponsable = empresaResponsable
	
	def set_empresaResponsable(self, empresaResponsable):
		self._empresaResponsable = empresaResponsable

	def get_empresaResponsable(self):
		return self._empresa_responsable

