def narysuj_plansze(stan_gry):
    print('{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(*stan_gry))

    # print()
    # print(f'{stan_gry[0]}|{stan_gry[1]}|{stan_gry[2]}\n-----\n{stan_gry[3]}|{stan_gry[4]}|{stan_gry[5]}\n-----\n{stan_gry[6]}|{stan_gry[7]}|{stan_gry[8]}')


def zapytaj_gracza_o_liczbe():
    pass


def sprawdz_czy_wygrana(stan_gry):
    pass


if __name__ == '__main__':
    stan_gry = [' '] * 9
    obecny_gracz = 'X'
    narysuj_plansze(stan_gry)


# string = 'fghfhgjh {} hjkhlh'.format(zmienna)
