"""
• Utwórz klasę opisującą pracownika, zaproponuj atrybuty i zainicjuj je
• Utwórz klasę kierownika zespołu wykorzystując relację dziedziczenia (kierownik jest
też pracownikiem)
• Zmień zachowanie wybranych metod, wykorzystując zachowanie oryginalne
"""


class Pracownik:

    def __init__(self, imie, nazwisko, stanowisko, chec_do_pracy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.chec_do_pracy = chec_do_pracy

    def zwroc_imie(self):
        return f'{self.imie} {self.nazwisko}'

    def __repr__(self):
        return ' '.join([self.imie, self.nazwisko, self.stanowisko])


class ManagerMixin:

    def zarzadzaj(selfself):
        print('Zarządzam')


class Kierownik(Pracownik, ManagerMixin):

    def __init__(self, imie, nazwisko, chec_do_pracy):
        super().__init__(imie, nazwisko, 'kierownik', chec_do_pracy)
        self.lista_pracownikow = []

    def zwroc_imie(self):
        return f'Kierownik {super().zwroc_imie()}'

    def dodaj_pracownika(self, pracownik):
        self.lista_pracownikow.append(pracownik)

    def wypisz_imiona_pracownikow(self):
        imiona = ''
        for osoba in self.lista_pracownikow:
            imiona += ' ' + osoba.imie
        print(imiona)
        print(self.lista_pracownikow)


pracownik_1 = Pracownik("Jan", "Kowalski", "operator wózka", False)
print(pracownik_1.zwroc_imie())

pracownik_2 = Pracownik("Janek", "Kowalewski", "operator wózka", False)

kierownik = Kierownik('Adam', 'Adamski', True)
print(kierownik.zwroc_imie())

kierownik.dodaj_pracownika(pracownik_1)
kierownik.dodaj_pracownika(pracownik_2)

kierownik.wypisz_imiona_pracownikow()

kierownik.zarzadzaj()
