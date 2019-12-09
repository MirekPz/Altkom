"""
PE2 Wykorzystując instrukcje sterujące (break, continue) stwórzmy pętlę, która która dla zmiennej
(np. i) zmieniającej się od 0 do 1000 wyświetli wartość i, ale:
a) jeśli wartość jest podzielna przez 3 to nie wyświetli tej wartości
b) jeśli wartość jest podzielna przez 77 to przerwie działanie pętli
"""


i = 0
while i < 1000:

    i += 1

    if i % 3 == 0:
        continue

    if i % 77 == 0:
        break

    print(i, end=' ')


