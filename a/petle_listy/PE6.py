"""
PE6 Wypisz wartość sinusa dla kątów w zakresie 1 - 90
"""

import math

print(math.sin(0))
print(math.sin(math.pi/2))
print()

for i in range(91):
    print(math.sin(math.radians(i)))

