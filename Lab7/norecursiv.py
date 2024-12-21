def count(lst):
    n = 0
    stack = lst
    while stack:
        st = stack.pop()
        if isinstance(st, list):
            stack.extend(st)
            n+=1
        else:
            n+=1
    return n
print(count([1, 2, [3, 4, [5]]]))