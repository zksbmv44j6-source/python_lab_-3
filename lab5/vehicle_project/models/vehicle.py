class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"

    def accelerate(self, value):
        self._speed += value

    def brake(self, value):
        self._speed = max(0, self._speed - value)

    def stop(self):
        self._speed = 0