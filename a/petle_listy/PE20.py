"""
PE20 Dla listy a:
a = ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]
i listy b:
b = ['cde', 'b', 33, 'gh', 'g']
c = []
zrób pętlę w której sprawdzimy czy każdy element z listy b znajduje się w liście a
i jeśli nie to doda go do listy c
"""

a = ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]
b = ['cde', 'b', 33, 'gh', 'g']
c = []

for x in b:
    if x not in a:
        c.append(x)

print(c)

c = []
c = [x for x in b if x not in a]
print(c)
