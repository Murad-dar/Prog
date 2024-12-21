def x(i):
    if i == 1:
        return 1
    if i == 2:
        return -1 / 8
    x2 = 1  # x_1
    x1 = -(1 / 8)  # x_2
    for i in range(3, i + 1):
        xi = ((i - 1) * x1) / 3 + ((i - 2) * x2) / 4
        x2 = x1
        x1 = xi
    return xi
print(x(5))