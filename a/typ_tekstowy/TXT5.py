"""
TXT5 Mamy zdanie i chcemy podzielić je w miejscu pierwszej znalezionej spacji
używając splicingu (uzyskamy raz część przed spacją a raz od spacji do końca)
"""
txt = "Ala ma kota i psa."

print(txt.split(" ", 1))
print(txt.split(" ", 2))
print(txt.split(" ", 3))
print(txt.split(" ", 4))
