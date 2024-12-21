def x(i):
    if i == 1:
        return 1
    if i == 2:
        return -1/ 8
    return ((i - 1) * x(i - 1)) / 3 + ((i - 2) * x(i - 2)) / 4
print(x(5))