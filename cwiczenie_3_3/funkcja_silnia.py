def silnia(n):
    i = 0
    silnia = 1
    while i < n:
        i += 1
        silnia *= i
    return silnia


print(silnia(5))
