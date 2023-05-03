"""Program automatyzuje grę w zgadywanie liczby."""

import random

a = int(input("Podaj początek zakresu liczb: "))
b = int(input("Podaj koniec zakresu liczb: "))

if a >= b:
    print("Podano błędny zakres.")
elif len(range(a, b)) < 3:
    print("Przedział liczb jest za mały.")

number = random.randint(a, b)
chance = 1

win = False

while chance <= 3:
    choice = input("Wybierz liczbę z podanego zakresu od " + str(a) + " do " + str(b) + " : " )
    if choice.isnumeric():
        choice = int(choice)
        if choice == number:
            print("Wygrałeś, brawo!")
            win = True
            break
        elif choice > b or choice < a:
            print("Podano liczbę spoza zakresu!")
        elif choice > number:
            print("Za duża liczba, próbu dalej!")
        elif choice < number:
            print("Za mała liczba, próbuj dalej!")
    chance += 1
if not win:
    print("Przegrales - szkoda.")