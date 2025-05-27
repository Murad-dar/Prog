from premises_calculator.premise import Premise
from premises_calculator.apartment import Apartment

class Building(Premise):
    def __init__(self):
        self._apartments = []

    @property
    def apartments(self):
        return self._apartments

    def add_apartment(self, apartment: Apartment):
        """Добавляет квартиру в дом."""
        self.apartments.append(apartment)

    def calculate_area(self):
        """Рассчитывает общую площадь дома."""
        return sum(apartment.calculate_area() for apartment in self.apartments)

    def calculate_heating_power(self, k=40):
        """Рассчитывает суммарную тепловую мощность для дома."""
        return sum(apartment.calculate_heating_power(k) for apartment in self.apartments)

    def __str__(self):
        return f"Дом: Площадь = {self.calculate_area():.2f} м², Мощность = {self.calculate_heating_power():.2f} Вт"

    def __eq__(self, other):
        if not isinstance(other, Building):
            return False
        if len(self.apartments) != len(other.apartments):
            return False
        return all(a1 == a2 for a1, a2 in zip(self.apartments, other.apartments))