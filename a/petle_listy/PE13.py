"""
PE13 Narysuj trójkąt wyrównany do prawej
  X
 XX
XXX
"""

h = int(input("Podaj wysokość trójkąta: "))

for i in range(h):
    print(" " * (h-i-1) + "X" * (i+1))
