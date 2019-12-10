"""
PE19 Mamy listę moja_lista = [-2, 4, -1, 66, 5, 0, -1]
chcemy mieć nową listę
taką, że jeśli element jest mniejszy niż 0 to dodamy do niego 5
a jeśli jest większy równy 0 to dodamy do niego 100
"""

moja_lista = [-2, 4, -1, 66, 5, 0, -1]

nowa_lista = [x + 5 if x < 0 else x + 100 for x in moja_lista]

print(nowa_lista)
