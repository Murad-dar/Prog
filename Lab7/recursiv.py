def count(lst):
    n = 0
    for element in lst:
        if isinstance(element,list):  # Если элемент — это список
            n += count(element)
            n+=1
        else:
            n += 1 
    return n
print(count([1, 2, [3, 4, [5]]]))