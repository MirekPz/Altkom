"""
PE15 Narysuj / stwórz trójkąt pascala (może być jako kolejno wyświetlane listy)

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
............
"""

h = int(input("Podaj wysokość trójkąta: "))

wiersz = []

for i in range(h):
    for j in range(i):
        wiersz.append(j+1)
        print(wiersz)
#    print(wiersz)

# ????????????????????

