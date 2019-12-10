"""
• Napisz program, który zweryfikuje, czy podany tekst jest palindromem
• Palindrom brzmi tak samo, niezależnie od tego, czy jest czytany od przodu, czy wspak
• Wielkość liter, znaki separatorów i znaki interpunkcyjne nie mają znaczenia
"""

# txt = 'Kajak'

txt = "Co mi dał duch? Cud, ład i moc."

for znak in txt:
    if not znak.isalpha():
        # print(znak)
        txt = txt.replace(znak, "")

txt = txt.lower()

palindrom = txt[-1::-1]

print(txt, palindrom)

if palindrom == txt:
    print("To jest palindrom\n")



# wariant 2 z list comprehensions:

zdanie = "Co mi dał duch? Cud, ład i moc."
litery = [litera for litera in zdanie.lower() if litera.isalpha()]
print("Palindrom" if litery == list(reversed(litery)) else "Nie palindrom")
