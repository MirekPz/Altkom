"""
PE14 Narysuj romb:
   X
  XXX
 XXXXX
XXXXXXX
 XXXXX
  XXX
   X

lub

 XX
XXXX
XXXX
 XX
"""

h = int(input("Podaj wysokość rombu nieparzystego: "))

for i in range(h//2):
    print(" " * ((h-i-1)) + "X" * (i+1) + "X" * i)
print(" " * (h//2) + "X" * h)
for i in range(h//2 - 1, -1, -1):
    print(" " * ((h-i-1)) + "X" * (i+1) + "X" * i)
