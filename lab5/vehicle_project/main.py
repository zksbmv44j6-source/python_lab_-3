from models.vehicle import Vehicle

car = Vehicle("Toyota", "Camry", 2024)

print(car.speed)
car.accelerate(60)
print(car.speed)
car.brake(20)
print(car.speed)
car.brake(100)
print(car.speed)

car.speed = 30
print(car.speed)

try:
    car.speed = -5
except ValueError as error:
    print("Ошибка:", error)

try:
    car.accelerate(-50)
except ValueError as error:
    print("Ошибка:", error)

print(car.speed)