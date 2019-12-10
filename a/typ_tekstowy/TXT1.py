"""
TXT1 Stwórz program, który policzy ile razy w podanym przez użytkownika zdaniu znajduje się
literka małe a?
Ile razy w podanym zdaniu znajduje się mała lub duża litera a?
"""

txt = input("Podaj zdanie: ")
print(txt.count('a'))
print(txt.lower().count('a'))
