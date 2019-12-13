import os

print(os.getcwd())

print(os.path.normpath(os.path.join(
    "/", 'home', 'altkom', 'Pulpit', '..')))

os.system('ls')

os.system('ls > a.txt')
