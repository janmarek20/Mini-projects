import matplotlib.pyplot as plt

#Zaczytanie wyników wyborów z oficjalnych plików wyborów prezydenckich 2020.

with open("kandydaci_utf8.csv", "r", encoding='utf8') as k:
    lines_n = k.readlines()
    nazwiska = list()
    for line_n in lines_n:
        if line_n == lines_n[0]:
            continue
        line_n = line_n.split(";")
        nazwiska.append(line_n[1])
        print(line_n)
    print(nazwiska)
    with open("wyniki_gl_na_kand_po_wojewodztwach_utf8.csv", "r", encoding='utf8') as w:
        lines_w = w.readlines()
        wyniki = list()
        x = 24
        for kandydat in nazwiska:
            suma_glosow = 0
            for wojewodztwo in lines_w:
                if wojewodztwo == lines_w[0]:
                    continue
                wojewodztwo = wojewodztwo.split(";")
                suma_glosow = suma_glosow + int(wojewodztwo[x])
            wyniki.append(suma_glosow)
            x += 1

        print(wyniki)

#Wyniki wyborów przedstawione na wykresie słupkowym.

plt.bar(nazwiska, wyniki)
plt.title('Wyniki wyborów prezydenckich przedstawione na wykresie słupkowym')
plt.xticks(nazwiska)
plt.yticks(wyniki)
plt.show()

#Wyniki wyborów przedstawione na wykresie kołowym.

plt.pie(wyniki, labels = nazwiska, autopct = "%.2f %%")
plt.axis('equal')
plt.title('Wyniki wyborów prezydenckich przedstawione na wykresie kołowym')
plt.show()

#Wyniki kandydatów z uzyskaniem liczby głósów >= 1%.
nazwiska_2 = []
wyniki_2 = []
x = 0

for i in nazwiska:
    if wyniki[x] / sum(wyniki) >= 0.01:
        nazwiska_2.append(i)
        wyniki_2.append(wyniki[x])
    x = x + 1

plt.bar(nazwiska_2, wyniki_2)
plt.title('Wyniki kandydatów z uzyskaniem liczby głósów >= 1%')
plt.xticks(nazwiska_2)
plt.yticks(wyniki_2)

plt.show()


