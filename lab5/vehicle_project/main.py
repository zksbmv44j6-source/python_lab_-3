from models.vehicle import Vehicle

car = Vehicle("Toyota", "Camry", 2024)
print(car)

car.accelerate(60)
print(car)
print(f"В гараже: {car}")