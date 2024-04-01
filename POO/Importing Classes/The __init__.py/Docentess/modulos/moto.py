class Moto:

	count = 0

	def __init__(self, manufacturador, modelo, color, año, km, dueño):
		Moto.count += 1
		self.manufacturador = manufacturador
		self.modelo = modelo
		self.color = color
		self.año = año
		self.km = km
		self.dueño = dueño

	def descripcion(self):
		print(f"\nLa moto de {self.dueño} es una {self.manufacturador} {self.modelo}, de color {self.color}, año: {self.año} y con {self.km} km\n")

	def andar(self):
		print("\t*La moto está andando")

	def leerOdometro(self):
		print(f"\t*La moto tiene {self.km} km")

	def incrementarOdometro(self, km):
		if km < self.km:
			print("\nNo puede disminuir el valor del kilometraje\n")
		else:
			self.km = km

	def cantidad_Docentes(self):
		print(f"\t*Hay {Moto.count} docentes con moto")