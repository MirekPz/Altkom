def moja_funkcja(a, *args):
    print("args: ", args)
    print("args: ", *args)
    for element in args:
        a = a * element
    return a


print(moja_funkcja(1, 3, 4, 2, 9))
