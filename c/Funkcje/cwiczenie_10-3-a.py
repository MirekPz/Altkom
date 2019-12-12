"""
stwórz funkcję, która przyjmie jako argument listę słowników (listę osób) oraz literę i zwróci listę,
w której nie znajdzie się osoba, której imię zaczyna się na daną literę
"""
from os import remove

dane = [{'imię': 'Jan', 'nazwisko': 'Kowalski'},
        {'imię': 'Anna', 'nazwisko': 'Kowalska'}]


def filtruj_po_imieniu(lista, litera):
    """
    Funkcja  usuwa z listy osoby, których imię zaczyna się od litery

    argumenty:
        lista : list - lista słowników osób (klucze: imnię, nazwisko)
        litera : str - pierwsza litera imienia używana do filtrowania

    zwraca:
        lista : list - lista osób pomniejszona o usuniętą osobę

    (funkcja zwraca nową listę słowników, pozbawioną pozycji z imionami zaczynającymi się na określoną literę,
    która jest jednocześnie parametrem funkcji)
    """
    osoby = lista.copy()
    # drugi sposób:   osoby = lista[:]

    print(osoby)
    for osoba in lista:
        if osoba['imię'][0] == litera:
            print(osoba['imię'][0])
            osoby.remove(osoba)
    print(osoby)
    return osoby


wynik = filtruj_po_imieniu(dane, 'A')
print(dane, wynik)

while True:
    litera = input("\nPodaj literę: ").upper()
    print(filtruj_po_imieniu(dane, litera))
    if litera == "Q":
        break
