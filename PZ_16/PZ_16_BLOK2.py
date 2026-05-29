# Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колес, а классы- наследники будут иметь свои уникальные свойства и методы.

class TransportVehicle:
    def __init__(self, max_speed, wheel_count):
        self.max_speed = max_speed
        self.wheel_count = wheel_count

    def info(self):
        return f"Макс. скорость: {self.max_speed} км/ч, Кол-во колес: {self.wheel_count}"


class Car(TransportVehicle):
    def __init__(self, max_speed, wheel_count, brand, model):
        super().__init__(max_speed, wheel_count)
        self.brand = brand
        self.model = model

    def info(self):
        base = super().info()
        return f"Автомобиль {self.brand} {self.model}. {base}"


class Motorcycle(TransportVehicle):
    def __init__(self, max_speed, wheel_count, brand, has_sidecar=False):
        super().__init__(max_speed, wheel_count)
        self.brand = brand
        self.has_sidecar = has_sidecar

    def info(self):
        base = super().info()
        sidecar = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотоцикл {self.brand}. {base}. {sidecar}"


# Тестовые запуски
print("=== Тест наследования ===")
car = Car(220, 4, "Toyota", "Camry")
moto = Motorcycle(180, 2, "Yamaha", True)

print(car.info())
print(moto.info())