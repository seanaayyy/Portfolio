# name, alcoholic, available
# getters, initializer, setAvailable

class Ingredient:
    available: bool

    def __init__(self, name: str, available: bool = False, measurement = ''):
        self.name = name
        self.available = available
        self.measurement = measurement

    def to_string(self):
        return self.name

    def get_name(self):
        return self.name

    def get_available(self):
        return self.available

    def get_measurement(self):
        return self.measurement

    def set_available(self, available):
        self.available = available

