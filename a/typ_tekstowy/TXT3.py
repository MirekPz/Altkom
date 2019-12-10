"""
TXT3 Stwórz tekst witający użytkownika w zależności od tego jakie imię
użytkownik wprowadzi - należy użyć formatowania
"""

name = input("Podaj Twoje imię: ")
if name[-1] == 'a':
    print(f"Dzień dobry pani {name[0:len(name)-1]}o")
else:
    print(f"Dzień dobry panie {name}")
