"""
PE5 Dla zadanej listy:
['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]
dla wszystkich elementów prócz pierwszego i ostatniego wypisz ten element i jego typ
przykładowo dla pierwszego elementu:
a <type str>
"""

lista= ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]

for element in range(1, len(lista)-1):
    print(lista[element], type(lista[element]))


print(lista[1:-1])
