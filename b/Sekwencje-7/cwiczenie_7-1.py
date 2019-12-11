"""
Napisz program, który w oparciu o podaną pełną nazwę utworzy jej skrót, np. zamieni
United Nations Educational, Scientific and Cultural Organization na UNESCO
"""

name = "United Nations Educational, Scientific and Cultural Organization"
words = name.split()

print(words)

skrot_jako_lista = [word[0] for word in words if word[0].isupper()]

skrot = "".join(skrot_jako_lista)

print(skrot)

