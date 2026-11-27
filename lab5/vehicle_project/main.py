from models.vehicle import Vehicle

car1 = Vehicle("Toyota", "Camry", 2024)
car2 = Vehicle("Lada", "Vesta", 2023)

print(car1.brand, car1.model, car1.year, car1._speed)
print(car2.brand, car2.model, car2.year, car2._speed)

car1._speed = 50
print(car1._speed)
print(car2._speed)