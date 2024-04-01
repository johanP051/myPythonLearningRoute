class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0
    
    def description(self):
        name = f"{self.manufacturer} {self.model} {self.year}"
        print(name)
        
    def odometer_read(self):
        print(f"This car has recorred {self.odometer} miles")
    
    def fillTank(self):
        print('The tank is filling')
 
