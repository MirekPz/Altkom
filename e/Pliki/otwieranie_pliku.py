plik = open('example_txt_file.dmo', 'r')
zawartosc = plik.read()
print(zawartosc)
plik.close()

input('drugi:')

# with open

with open('example_txt_file.dmo') as file:
    print(file.read())
