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
    
    return stan_gry

def sprawdz_czy_wygrana(stan_gry):
    wygrane = [(0, 1, 2), (0, 3, 6), (3, 4, 5), (6, 7, 8), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    pass


def zmien_gracza(obecny_gracz):
    pass


if __name__ == '__main__':
    stan_gry = [x for x in range(9)]  # " " * 9
    obecny_gracz = (1, 'X')  # (2, 'O')
    # narysuj_plansze(stan_gry)
    liczba = zapytaj_gracza_o_liczbe(obecny_gracz, stan_gry)
    print(liczba)

    stan_gry[liczba] = 'X'
    nowy_stan_gry = aktualizuj_gre(stan_gry, obecny_gracz, liczba)
