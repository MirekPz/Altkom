"""
PE12 Narysuj trójkąt
X
XX
XXX
"""

h = int(input("Podaj wysokość trójkąta: "))

for i in range(h):
    print("X" * (i+1))
