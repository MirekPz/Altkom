with open('example_txt_file.dmo') as f:
    zawartosc = f.readlines()
    x = None; y = None; z = None
    for line in zawartosc:
        print(line)
