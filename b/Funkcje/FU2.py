"""
FU2 Stwórz funkcję, która dla zadanej listy wartości liczbowych będzie liczyła ich sumę
średnią, medianę, odchylenie standardowe
i zwróci te wartości w postaci krotki
"""


def statystyka(lista):
    suma=0
    for element in lista:
        suma += element
    srednia = suma/len(lista)
    if len(lista) % 2 == 1:
        mediana = lista[len(lista)//2]
    else:
        mediana = (lista[len(lista)//2 - 1] + lista[len(lista)//2])/2
    print(suma, srednia, mediana)


statystyka([1, 2, 3, 4, 5])
statystyka([1, 2, 3, 4, 5, 6])


liczby = [1, 2, 3, 4, 5, 6]
print(liczby)
print(*liczby)   # rozpakowywanie listy
