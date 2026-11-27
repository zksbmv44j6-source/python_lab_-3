from models.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def get_info(self):
        base = super().get_info()
        return f"{base}, грузоподъёмность: {self.max_load} т"