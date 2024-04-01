class Bicicleta:
    
    count = 0

    def __init__(self, marca, color, mecanismo, tipo, dueño):
        self.marca = marca
        self.color = color
        self.mecanismo = mecanismo
        self.tipo = tipo
        self.dueño = dueño
        Bicicleta.count +=1 #contador de cantidad de veces que se instancia la clase
    
    def descripcion(self):
        print(f"\nLa bicicleta del docente {self.dueño}, de marca {self.marca}, color: {self.color}, con mecanismo de {self.mecanismo} y tipo: {self.tipo}\n")

    def andar(self):
        print("\t*La bicicleta está andando")

    def cantidad_Docentes(self):
        print(f"\t*Hay {Bicicleta.count} docentes con bicicleta")