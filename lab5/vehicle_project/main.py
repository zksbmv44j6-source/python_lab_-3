from models.vehicle import Vehicle
from models.car import Car

car = Car("Toyota", "Camry", 2024, 4)

print(car.doors)
car.accelerate(60)
car.brake(20)
print(car.speed)
print(car.get_info())
print(car)
print(isinstance(car, Car), isinstance(car, Vehicle))