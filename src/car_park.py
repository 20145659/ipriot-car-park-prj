class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."
