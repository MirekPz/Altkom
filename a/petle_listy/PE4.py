"""
PE4 Dla listy zawierającej kilka wartości liczbowych stwórz kod, który policzy sumę tych
elementów (można użyć polecenia moja_lista.pop)
"""
lista = [2, 3, 9, 12, 10]
suma = 0
for i in range(len(lista)):
    suma += lista[i]

print("Suma = ", suma)
