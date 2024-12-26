import random

def random_number_generator(start, end):
    """Генератор случайных чисел в заданном диапазоне."""
    while True:
        yield random.randint(start, end)