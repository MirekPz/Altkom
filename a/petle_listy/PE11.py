"""
PE11 Podobnie jak w poprzednim zadaniu, tworzymy pusty kwadrat o zadanej wielkości
Przykładowo dla wielkości 4:
XXXX
X  X
X  X
XXXX
"""

a = int(input("Podaj bok kwadratu: "))

for i in range(a):
    if i == 0 or i == a-1:
        print("X" * a)
    else:
        print("X" + " " * (a-2) + "X")
