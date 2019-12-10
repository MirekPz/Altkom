"""
TXT4 Podziel tekst wprowadzony przez użytkownika na poszczególne wyrazy,
lub na poszczególne zdania
"""

txt = input("Wpisz dowolne zdanie lub zdania: ")
new_txt = txt.split(" ")
print(new_txt)
without_dot = txt.replace(".", "")
new_txt_2 = without_dot.split(" ")
print(new_txt_2)

zdania = txt.split(".")
print(zdania)
print(zdania[0:len(zdania) - 1])

# zdania.pop() - usuwa ostatni element
