"""
PE10 Stwórz kwadrat o określonej wielkości (wprowadzanej z klawiatury) z litery X.
Przykładowo dla wielkości 3 kwadrat powinien wyglądać jak poniżej:
XXX
XXX
XXX
1) dodając pojedyncze litery X do siebie i printując w zagnieżdżonych pętlach
2) wykorzystując zamiast jednej z pętli mnożenie stringów
"""

a = int(input("Podaj bok kwadratu: "))

for i in range(a):
    for j in range(a):
        print('X', end='')
    print()

print("-"*30)
print("Mnożenie stringów:")
for i in range(a):
    print('X' * a)
