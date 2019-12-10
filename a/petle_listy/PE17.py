"""
PE17
dla stopni C = [12, 33, 15, 25]
oblicz temperaturę w Kelwinach (wyrażeniem listowym, + 273.15)
"""

C = [12, 33, 15, 25]
K = [c + 273.15 for c in C]

print("Temperatura w Kelwinach: ", K)
