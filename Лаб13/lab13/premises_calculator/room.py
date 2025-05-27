from premises_calculator.premise import Premise

class Room(Premise):
    def __init__(self, length: float, width: float, height: float):
        self._length = length
        self._width = width
        self._height = height

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = value

    def calculate_area(self):
        """Рассчитывает площадь комнаты."""
        return self.length * self.width

    def calculate_heating_power(self, k=40):
        """Рассчитывает тепловую мощность для обогрева комнаты."""
        volume = self.calculate_area() * self.height
        return volume * k

    def __str__(self):
        return f"Комната: Площадь = {self.calculate_area():.2f} м², Мощность = {self.calculate_heating_power():.2f} Вт"

    def __eq__(self, other):
        if not isinstance(other, Room):
            return False
        return (abs(self.length - other.length) < 0.001 and
                abs(self.width - other.width) < 0.001 and
                abs(self.height - other.height) < 0.001)