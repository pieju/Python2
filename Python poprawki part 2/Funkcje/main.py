#4 zadanie do poprawy 
def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        print("Nie można dzielić przez zero!")
        return None

def wypisz_menu():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

def pobierz_liczby():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    return a, b

while True:
    wypisz_menu()
    wybor = input("Twój wybór: ")

    if wybor == "1":
        a, b = pobierz_liczby()
        wynik = dodawanie(a, b)
        print("Wynik dodawania:", wynik)
    elif wybor == "2":
        a, b = pobierz_liczby()
        wynik = odejmowanie(a, b)
        print("Wynik odejmowania:", wynik)
    elif wybor == "3":
        a, b = pobierz_liczby()
        wynik = mnozenie(a, b)
        print("Wynik mnożenia:", wynik)
    elif wybor == "4":
        a, b = pobierz_liczby()
        wynik = dzielenie(a, b)
        if wynik is not None:
            print("Wynik dzielenia:", wynik)
    elif wybor == "5":
        break
    else:
        print("Nieprawidłowy wybór! Wybierz ponownie.")
