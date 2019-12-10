"""
PE7 Wypisz wartość sinusa /cosinusa dla kątów w zakresie 1 – 90, rodzaj funkcji
trygonometrycznej użytkownik ma podać z klawiatury
"""

import math

funkcja = input("Podaj funkcję trygonometryczną: [S]inus, [C]osinus  ").lower()

if funkcja == 's':
    for i in range(91):
        print(round(math.sin(math.radians(i)), 4))
elif funkcja == 'c':
    for i in range(91):
        print(round(math.cos(math.radians(i)), 4))
else:
    print("Nie wybrano właściwej funkcji!")


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
# y = np.sin(x)
# plt.plot(x, y)
# plt.show
# plt.show()
