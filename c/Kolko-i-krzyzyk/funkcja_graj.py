def narysuj_plansze(stan_gry):
    print('{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(*stan_gry))

    # print()
    # print(f'{stan_gry[0]}|{stan_gry[1]}|{stan_gry[2]}\n-----\n{stan_gry[3]}|{stan_gry[4]}|{stan_gry[5]}\n-----\n{stan_gry[6]}|{stan_gry[7]}|{stan_gry[8]}')


def zapytaj_gracza_o_liczbe(gracz, plansza):
    """ Rysujemy planszę z liczbammi 0-8, potem pytamy gracza o liczbę

    """
    narysuj_plansze(plansza)
    return int(input('\nGracz {} gdzie chcesz wstawić {}: '.format(*gracz)))


def aktualizuj_gre(stan_gry, gracz, pozycja):
    stan_gry[pozycja] = gracz[1]  # krotka o indeksie 1
    return stan_gry

def sprawdz_czy_wygrana(stan_gry):
    wygrane = [(0, 1, 2), (0, 3, 6), (3, 4, 5), (6, 7, 8), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for wygrana in wygrane:
        if stan_gry[wygrana[0]] == stan_gry[wygrana[1]] == stan_gry[wygrana[2]]:
            return True
    return False

def zmien_gracza(obecny_gracz):
    return (2, 'O') if obecny_gracz[0] == 1 else (1, 'X')

def graj():
    stan_gry = [x for x in range(9)]  # " " * 9
    obecny_gracz = (1, 'X')  # (2, 'O')
    koniec = False
    while not koniec:
        liczba = zapytaj_gracza_o_liczbe(obecny_gracz, stan_gry)
        print(liczba)
        stan_gry = aktualizuj_gre(stan_gry, obecny_gracz, liczba)
        obecny_gracz = zmien_gracza(obecny_gracz)
        print(obecny_gracz)

        koniec = sprawdz_czy_wygrana(stan_gry)


if __name__ == '__main__':
    graj()
