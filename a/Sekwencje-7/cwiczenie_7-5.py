"""
• Napisz program, który utworzy macierz jednostkową
• Wykorzystaj wyrażenie listowe
• Macierz jednostkowa 4 x 4 ma postać:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
"""

n = int(input("Rozmiar macierzy: "))
lista=[]

for i in range(n):
    lista.append(0)
    for j in range(n):
        [lista.append(0)]

print(lista)
# ??????????????????????/

# list comprehension;
print([[0 for i in range(5)] for j in range(5)])
