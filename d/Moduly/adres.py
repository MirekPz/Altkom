class Adress:

    def __init__(self, ulica, kod, miasto):

        self.ulica = ulica
        self.kod = kod
        self.miasto = miasto

    @staticmethod
    def _wyswietl():
        print("Moduł adres")
