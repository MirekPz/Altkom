"""
PE18
Stwórz listę, która będzie zawierała tylko dodatnie elementy z listy a
(wykorzystaj wyrażenie listowe)
"""

a = [3, -3, 7, 2, 21, -99, -3, 2]

dodatnie = [x for x in a if x > 0]

print(dodatnie)
