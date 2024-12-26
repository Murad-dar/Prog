# main.py

import typer
from lab7 import count, count_non_recursive
from lab8 import make_calc
from lab9 import random_number_generator

app = typer.Typer()

@app.command()
def count_elements(lst: str, recursive: bool = True):
    """Подсчет элементов в списке."""
    import ast
    parsed_list = ast.literal_eval(lst)
    if recursive:
        result = count(parsed_list)
    else:
        result = count_non_recursive(parsed_list)
    typer.echo(f"Количество элементов: {result}")

@app.command()
def calculator(operation: str, initial: float = 0):
    """Калькулятор с заданной операцией."""
    calc = make_calc(operation, initial)
    while True:
        value = typer.prompt("Введите число (или 'exit' для выхода)")
        if value.lower() == 'exit':
            break
        calc_value = calc(float(value))
        typer.echo(f"Текущий результат: {calc_value}")

@app.command()
def random_numbers(start: int, end: int, count: int):
    """Генерация случайных чисел."""
    generator = random_number_generator(start, end)
    numbers = [next(generator) for _ in range(count)]
    typer.echo(f"Случайные числа: {numbers}")

if __name__ == "__main__":
    app()