class Vehicle:
    LicenseCode = ""
    serialCode = ""
    face = ""
    def trunOnAirConditioner(self):
        print("Trun On :Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.trunOnAirConditioner()
Pickup1 = Pickup()
Pickup1.trunOnAirConditioner()
van1 = Van()
van1.trunOnAirConditioner()
estatecar =Estatecar()
estatecar.trunOnAirConditioner()