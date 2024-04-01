#__init__.py lleva la sintaxis package.module

from modulos.bicicleta import Bicicleta
from modulos.moto import Moto

bici = Bicicleta("Scott", "verde", "cambios", "carrera", "Mary Contreras")
bici.descripcion()
bici.cantidad_Docentes()

bici2 = Bicicleta("Venzo", "Blanca", "sin cambios", "Híbrida", "Robick Serrano")
bici2.descripcion()
bici2.cantidad_Docentes()


moto = Moto("Yamaha", "FZ-25", "Negro", 2020, 80000, "Nicolás Reyes")
moto.descripcion()
moto.leerOdometro()

#Tratando de disminuir el kilometraje
moto.incrementarOdometro(10000)
moto.leerOdometro()

moto.incrementarOdometro(90000)
moto.leerOdometro()

moto.cantidad_Docentes()

