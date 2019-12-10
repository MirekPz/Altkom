"""
PE1 Wypisz wszystkie liczby nieparzyste od 0 do 1000 (linia po linii), korzystając z pętli while
"""

i = 0
while i < 1000:
    i += 1
    if i % 2 == 1:
        print(i, end='\t')
    if i % 100 == 0:
        print()
