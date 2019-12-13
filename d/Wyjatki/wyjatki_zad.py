class PunktPomiarowy:

    def __init__(self, x, y, z):

        self.x = self._sprobuj_skonwertowac(x, 'x')
        self.y = self._sprobuj_skonwertowac(y, 'y')
        self.z = self._sprobuj_skonwertowac(z, 'z')


    def _sprobuj_skonwertowac(self, wartosc, nazwa):

        try:
            skonwertowane = float(wartosc)
        except ValueError as opis_bledu:
            print("Błąd konwersji: ", opis_bledu)

        return skonwertowane

    def __str__(self):
        return f'Punkty pomiarowe --> \tx: {self.x} \ty: {self.y} \tz: {self.z}'

punkt1 = PunktPomiarowy(5,10,15)
print(punkt1)


punkt3 = PunktPomiarowy('x', 1, 1)

punkt2 = PunktPomiarowy('a', 'b', 'c')
