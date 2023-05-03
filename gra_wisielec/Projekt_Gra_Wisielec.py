import random

#Zautomatyzowana gra Wisielec

word = input("Podaj słwo do gry w Wisielca: ")
word = list(word.lower())
print(word)

search_word = []
for i in word:
    search_word.append("")

print(search_word)

numbers = set(range(97,123))
print(numbers)

letters = list()
for i in numbers:
    letters.append(chr(i))
print(letters)

win = False
step = 1
rounds = 36

while step <= rounds:
    print("Jest to próba numer " + str(step) + " z " + str(rounds) + ". ", end="")
    pick_letter = random.choice(letters)
    print("Wylosowano " + pick_letter + ". ", end="")
    if pick_letter in word:
        print("Brawo, litera " + pick_letter + " należy do szukanego wyrazu: ", end="")
        x = 0
        for i in word:
            if i == pick_letter:
                search_word[x] = pick_letter
            x = x + 1
            print(search_word)

        if word == search_word:
            print("Wygrana!")
            win = True
            break
    elif pick_letter not in word:
        print("Próbuj dalej!")
    step += 1
if not win:
    print("Przegrana.")




