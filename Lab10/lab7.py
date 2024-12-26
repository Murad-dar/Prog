# lab7.py

def count(lst):
    """Подсчет числа элементов в списках, включая вложенные списки (рекурсивно)."""
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += count(item)  # Рекурсивный вызов для вложенных списков
        else:
            total += 1
    return total

def count_non_recursive(lst):
    """Подсчет числа элементов в списках, включая вложенные списки (без рекурсии)."""
    stack = [lst]
    total = 0
    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, list):
                stack.append(item)
            else:
                total += 1
    return total