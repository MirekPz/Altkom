kapital = int(input("Kwota lokaty: "))
procent = int(input("Oprocentowanie roczne: "))
lata = int(input("Na ile lat lokata: "))

kwota = round(kapital * (1 + procent/100)**lata, 2)

print(kwota)
