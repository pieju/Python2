#zadanie 3
import random 
x = random.randint(0,100)

while(True):
    a = int(input("Podaj liczbe"))
    if a == x:
        print("brawo")
        c = input("Napisz tak jesli chcesz zagrac ponownie")
        if c == "tak":
                x = int(input("Podaj Liczbe"))
                continue 
        else:
                break
    elif a < x:
         print("Twoja liczba jest mniejsza od szukanej")
    elif a > x:
         print("Twoja liczba jest wieksza od szukanej")
