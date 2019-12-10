"""
Napisz program, który w oparciu o podaną pełną nazwę utworzy jej skrót,
np. zamieni United Nations Educational, Scientific and Cultural Organization na UNESCO
"""

name = "United Nations Educational, Scientific and Cultural Organization"

# skrot = name[0]
# pozycja_spacji = name.find(" ")
# print(skrot)
# print(name.find(" "))
# print(name[pozycja_spacji + 1])

wyrazy = name.split(" ")
print(wyrazy)

skrot=""
for wyraz in wyrazy:
    if wyraz[0].isupper():
        skrot += wyraz[0]

print(skrot)
