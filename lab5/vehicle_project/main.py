from models.vehicle import Vehicle

car1 = Vehicle("Toyota", "Camry", 2024)
car2 = Vehicle("Lada", "Vesta", 2023)

car1.accelerate(60)
print(car1.get_info(), car1._speed)
car1.brake(20)
print(car1._speed)
car1.brake(100)
print(car1._speed)

car2.accelerate(30)
print(car2._speed)
car2.stop()
print(car2._speed)