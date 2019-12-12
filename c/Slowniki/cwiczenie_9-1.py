"""
Napisz program, który podaną liczbę zapisze za pomocą cyfr rzymskich
"""

rzymskie = ['M', "CM", 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
arabskie = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

dict_liczby = dict(zip(arabskie, rzymskie))

print(dict_liczby)
wynik = ''

liczba = int(input("Podaj liczbę arabską od 1 do 4000: "))

for arabska in arabskie:
    while liczba >= arabska:
        liczba -= arabska
        wynik += dict_liczby[arabska]



print('Liczba rzymska:', wynik)
