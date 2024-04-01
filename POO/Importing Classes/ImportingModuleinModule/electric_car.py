#Como la clase ElectricCar depende de Car, entonces se importa Car en este módulo para que funcione al importar desde el archivo "Module into Module"
from car import Car
class Battery: #New class battery
    def __init__(self, battery=90):
        self.battery = battery
        self.length = 0
    
    def batteryPercentage(self): 
        print(f"\nCar has {self.battery}% of battery")
    
    def upgrade_Battery(self):
        if self.battery != 100:
            print("Battery is upgrading...")
            time.sleep(3)
            self.battery = 100
        else:
            Battery.batteryPercentage(self) #Se llama al método de una vez
            print("Battery is already upgraded")
    
    def distance(self):
        if self.battery == 90:
            self.length += 255
        elif self.battery == 100:
            self.length += 400
        print(f"This car can go about {self.length}Km with {self.battery}% of battery")

class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year) 
        self.battery = Battery()
    def fillTank(self):
        print("This is an ElectricCar, It doesn't uses a tank")
