from models.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def get_info(self):
        base = super().get_info()
        return f"{base}, дверей: {self.doors}"