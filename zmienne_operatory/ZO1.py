"""
ZO1 Stwórz kod, który obliczy na jaką wysokość wzniesie się samolot po x minutach (podanych
przez użytkownika), jeśli prędkość wznoszenia to 12 m/s. Pomiń maksymalną wysokość.
"""

v = 12  # m/s

x = int(input("Podaj liczbę minut: "))

h = v * x * 60

print(f'Samolot wzniesię się na {h} metrów.')
