animal = input("Podaj nazwę zwierzęcia: ")

if animal.lower() == "kot":
    food = "Karma dla kotów"
elif animal.lower() == "pies":
    food = "Karma dla psów"
elif animal.lower() == "ptak":
    food = "Karma dla kotów"
else:
    food = "Karma dla nieokreślonego zwierzaka"

print(food)
