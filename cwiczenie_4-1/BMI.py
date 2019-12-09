wzrost = float(input("Podaj wzrost [m]; "))
waga = float(input("Podaj wagę [kg]; "))

BMI = waga/wzrost**2

print(round(BMI, 2))

if BMI < 16:
    print("Wygłodzenie")
elif BMI <=16.99:
    print("Wychudzenie")
elif BMI <= 18.49:
    print("Niedowaga")
elif BMI <= 24.99:
    print("Wartość prawidłowa:")
elif BMI <= 29.99:
    print("Nadwaga")
elif BMI <= 34.99:
    print("I stopień otyłości")
elif BMI <= 39.99:
    print("II stopień otyłości (otyłość kliniczna)")
else:
    print("III stopień otyłości (otyłość skrajna)")

print(f"Przedział prawidłowej wagi dla określonego wzrostu:  [{round(18.49 * wzrost**2, 1)} , {round(24.99 * wzrost**2, 1)}]")


