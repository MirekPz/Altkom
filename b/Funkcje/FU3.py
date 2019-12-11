"""
FU3 Stwórz funkcję lambda, która zamieni stopnie Celsiusza na Kelwiny (+273)
"""
c = int(input("Podaj temperaturę w stopniach Celsjusza: [k = 273 + c] "))

k = lambda c : 273 + c

print(k(c))


li = [9, 5, 3, 3, 2]
print(*map(lambda x: x+273, li))
