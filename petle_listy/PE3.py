"""
PE3 Stwórz listę, która będzie zawierała liczby parzyste
podzielne przez 3 i mniejsze niż 100 (liczby podzielne przez 3 mają resztę z dzielenia równą 0)
"""

# print("a\bnormal")

list1 = []

for i in range(100):
    if i % 6 == 0:
        list1.append(i)
        print(i, end=' ')

print()
print(list1)
