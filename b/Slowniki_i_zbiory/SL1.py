"""
SL1 Stwórz słownik danych osobowych klienta
odpytaj klienta o jego imię nazwisko i wiek, dodaj je do słownika
"""

name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")
age = int(input("Podaj wiek: "))

customer = {}
customer['imię'] = name
customer['nazwisko'] = surname
customer['wiek'] = age

print("Dane klienta: ", customer)
