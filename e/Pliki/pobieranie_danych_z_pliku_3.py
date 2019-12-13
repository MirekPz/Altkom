wynikowa_lista = []

with open('example_txt_file.dmo') as f:
    zawartosc = f.readlines()
    x = None; y = None; z = None
    for line in zawartosc:
        if line.startswith('TA(X'):
            x = line.split(', ')[-2]
            x = float(x)
        elif line.startswith('TA(Y'):
            y = line.split(', ')[-2]
            y = float(x)
        elif line.startswith('TA(Z'):
            z = line.split(', ')[-2]
            z = float(x)
            wynikowa_lista.append((x, y, z))

print(wynikowa_lista)

wynikowa_lista2 = sorted(
    wynikowa_lista,
    key=lambda b: max([abs(a) for a in b]),
    reverse=True)

with open('wynik.csv', 'w') as f:
    for punkt in wynikowa_lista2:
#        f.write(';'.join(str(k) for k in punkt) + '\n')
        f.write('{};{};{}\n'.format(*punkt))

