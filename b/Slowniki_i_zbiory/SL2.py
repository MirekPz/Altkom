"""
SL2 Stwórz bazę klientów:
1) 3 x w pętli odpytamy o imię nazwisko i wiek (uzyskamy listę słowników)
2) Obliczmy sumę wieku klientów
3) Zmieńmy imię trzeciego klienta na 'Jan'
"""

customers = []

age_sum = 0

for i in range(3):
    customer = {}
    print(f"Klient nr: {i+1}")
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    age = int(input("Podaj wiek: "))
    customer['imię'] = name
    customer['nazwisko'] = surname
    customer['wiek'] = age
    customers.append(customer)
    age_sum += age

print()
print(customers)
print(age_sum)

print(customers[2])
print(customers[2]['imię'])
customers[2]['imię'] = 'Jan'

print(customers)

suma_wieku = 0
for customer in customers:
    suma_wieku += customer['wiek']
print(suma_wieku)
