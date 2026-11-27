from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle

car = Car("Toyota", "Camry", 2024, 4)
truck = Truck("КАМАЗ", "54901", 2023, 20)
moto1 = Motorcycle("Урал", "Турист", 2022, True)
moto2 = Motorcycle("Honda", "Shadow", 2021, False)

truck.accelerate(40)

print(car)
print(truck)
print(moto1)
print(moto2)