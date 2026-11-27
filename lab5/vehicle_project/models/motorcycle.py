from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        base = super().get_info()
        if self.has_sidecar:
            return f"{base}, с коляской"
        return f"{base}, без коляски"