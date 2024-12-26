def make_calc(operation, initial=0):
    """Замыкание-калькулятор, накапливающее результат."""
    result = initial

    def calc(value):
        nonlocal result
        if operation == "+":
            result += value
        elif operation == "-":
            result -= value
        elif operation == "*":
            result *= value
        elif operation == "/":
            result /= value
        return result

    return calc