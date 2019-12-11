"""
FU1 Stwórz funkcję, która będzie przyjmowała wartości imię nazwisko i wiek,
gdzie wiek będzie miał wartość domyślną 3 i wypisze je na ekranie
1) wywołaj funkcję z podaniem i bez podania wieku
2) przekaż funkcji wartości ze słownika
{'imie': 'Waldemar', 'nazwisko': 'Nowak', 'wiek': 23}
podczas wywołania
"""


def osoba(imie, nazwisko, wiek = 3):
    print(imie, nazwisko, wiek)


osoba('Jan', 'Kowalski')

osoba('Józef', "Nowak", 25)


print("\nad.2 -->  z rozpakowaniem słownika:   dwie gwiazdki")


def wypisz(imie, nazwisko, wiek=3):
    print(imie, nazwisko, wiek)


moj_slownik = {'imie': 'Waldemar', 'nazwisko': 'Nowak', 'wiek': 23}

wypisz(**moj_slownik)
wypisz(imie= 'Waldemar', nazwisko = 'Nowak', wiek = 23)
