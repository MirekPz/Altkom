"""
• Utwórz prostą klasę reprezentującą osoby
• Zaproponuj atrybuty jakie powinna posiadać ta klasa
• Zdefiniuj sposób tworzenia obiektów i zachowanie klas
"""

import datetime


class Osoba:

    def __init__(self, imie, nazwisko, plec, rok_urodzenia, wzrost=180, waga=100):

        self.nazwisko = nazwisko
        self.imie = imie
        self.plec = plec
        self.rok_urodzenia = rok_urodzenia
        self.wzrost = wzrost
        self.waga = waga

    def ile_lat(self):
        current_year = datetime.datetime.today().year
        return current_year - self.rok_urodzenia

    def __str__(self):
        if self.plec == True:
            return f'{self.imie} {self.nazwisko}, wiek: {self.ile_lat()}, płeć: M'
        else:
            return f'{self.imie} {self.nazwisko}, wiek: {self.ile_lat()}, płeć: K'

    #def __repr__(self):
    #    return '__'
    #def __len__(self):
     #   return 1


osoba_1 = Osoba('Jan', 'Kowalski', True, 1950)
osoba_2 = Osoba('Anna', 'Nowak', False, 1989, 170, 60)

print(osoba_1.imie, osoba_1.rok_urodzenia)
print(osoba_2.imie, osoba_2.rok_urodzenia)

print(osoba_2.ile_lat())

print()
print(osoba_1)
print(osoba_2)

print()
osoba_1 = Osoba('Jan', 'Kowalski', True, 1950 + 1)
print(osoba_1.imie, osoba_1.rok_urodzenia)
print(osoba_1)

print()
osoba_1 = Osoba('Jan', 'Kowalski', True, 2050)
print(osoba_1)
