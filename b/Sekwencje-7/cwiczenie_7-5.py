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

# lista=[]
#
# for i in range(n):
#     lista.append(0)
#     for j in range(n):
#         [lista.append(0)]

# list comprehension;
print([[0 for i in range(n)] for j in range(n)])

# print([[1 for i in range(5) if i==j else 0] for j in range(5)])
