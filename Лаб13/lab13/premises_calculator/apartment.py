from premises_calculator.premise import Premise
from premises_calculator.room import Room

class Apartment(Premise):
    def __init__(self):
        self._rooms = []

    @property
    def rooms(self):
        return self._rooms

    def add_room(self, length: float, width: float, height: float):
        """Добавляет комнату в квартиру."""
        self.rooms.append(Room(length, width, height))

    def calculate_area(self):
        """Рассчитывает общую площадь квартиры."""
        return sum(room.calculate_area() for room in self.rooms)

    def calculate_heating_power(self, k=40):
        """Рассчитывает суммарную тепловую мощность для квартиры."""
        return sum(room.calculate_heating_power(k) for room in self.rooms)

    def __str__(self):
        return f"Квартира: Площадь = {self.calculate_area():.2f} м², Мощность = {self.calculate_heating_power():.2f} Вт"

    def __eq__(self, other):
        if not isinstance(other, Apartment):
            return False
        if len(self.rooms) != len(other.rooms):
            return False
        return all(r1 == r2 for r1, r2 in zip(self.rooms, other.rooms))