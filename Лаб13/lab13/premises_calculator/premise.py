from abc import ABC, abstractmethod

class Premise(ABC):
    @abstractmethod
    def calculate_area(self):
        """Рассчитывает общую площадь помещения."""
        pass

    @abstractmethod
    def calculate_heating_power(self):
        """Рассчитывает тепловую мощность для обогрева."""
        pass