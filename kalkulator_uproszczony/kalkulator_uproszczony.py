"""Program wykonuje wskazaną przez użytkownika operacją mateamtyczną na dwóch liczbach."""

def dodawanie (a, b):
    suma = a + b
    return suma
    print(suma)

def odejmowanie (a, b):
    roznica = a - b
    return roznica
    print(roznica)

def mnozenie(a , b):
    iloczyn = a * b
    return iloczyn
    print(iloczyn)

def dzielenie (a, b):
    if b:
        iloraz = a / b
        return iloraz
        print(iloraz)
    else:
        print("Nie dzielimy przez 0.")

znak = input("Podaj rodzaj działania do wykonania: dodawanie: +, odejmowanie: -, mnożenie: * lub dzielenie: / :")
if znak not in ["+", "-", "*", "/"]:
    print("Błąd we wprowadzonych danych.")
else:
    liczby = input("Podaj 2 liczby do działania, oddzielone przecinkiem: ")
    liczby_2 = list(liczby.split(","))
    print(liczby_2)

    liczby_3 = []
    for i in liczby_2:
        liczby_3.append(float(i))
        print(liczby_3)

if znak == "+":
    wynik = dodawanie(liczby_3[0], liczby_3[1])

elif znak == "-":
    wynik = odejmowanie(liczby_3[0], liczby_3[1])

elif znak == "*":
    wynik = mnozenie(liczby_3[0], liczby_3[1])

elif znak == "/":
    wynik = dzielenie(liczby_3[0], liczby_3[1])

print("Wynik działania " + str(liczby_3[0]) + znak + str(liczby_3[1]) + " wynosi " + str(wynik) + ".")