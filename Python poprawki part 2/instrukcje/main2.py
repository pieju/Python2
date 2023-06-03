#1.3 zadanie do poprawy
import random

x = random.randint(0, 100)
shots = 0

while True:
    a = int(input("Podaj liczbę: "))
    shots += 1

    if a == x:
        print("Brawo! Zgadłeś liczbę po", shots, "strzałach.")
        c = input("Napisz 'tak', jeśli chcesz zagrać ponownie: ")
        if c == "tak":
            x = random.randint(0, 100)
            shots = 0
            continue
        else:
            break
    elif a < x:
        print("Twoja liczba jest mniejsza od szukanej.")
    elif a > x:
        print("Twoja liczba jest większa od szukanej.")
