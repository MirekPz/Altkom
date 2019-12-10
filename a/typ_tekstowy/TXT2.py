"""
TXT2 Stwórz tekst np. 'Ala ma kota' - zmień wielkość liter na duże, małe, tak żeby
wszystkie wyrazy zaczynały się od dużej litery i tak żeby wszystkie wyrazy zaczynały się
od małej i potem litery były duże np. aLA
"""

txt = 'Ala ma kota'
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.title().swapcase())
