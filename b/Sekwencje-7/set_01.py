"""
Są dwa sklepy zoologiczne, mamy listy zwierząt z tych sklepów, chcemy wiedzieć jakie zwierzęta można dostać
tylko w jednym z tych sklepów.
"""

sklep_1 = {'pies', 'kot', 'mysz'}
sklep_2 = {'pies', 'kot', 'papuga'}

wynik = (sklep_1 - sklep_2) | (sklep_2 - sklep_1)

print(sklep_1)
print(sklep_2)

print(sklep_1 - sklep_2)
print(sklep_2 - sklep_1)

print(wynik)

wynik_2 = sklep_1 ^ sklep_2
print(wynik_2)

sklep_1.difference_update(sklep_2)
print(sklep_1)
