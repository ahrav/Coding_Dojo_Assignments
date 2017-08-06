for num in range(100,100000):
    x = num // 2
    y = set([x])
    while x * x != num:
        x = (x / (n // x)) // 2
        if x in y:
            return False
            y.add(x)
    return True
