def Dodawanie(X: float, Y: float) -> float:
    """ Dodaje jedną liczbę do drugiej """
    return X + Y

def odejmowanie(X: float, Y: float) -> float:
    """ Odejmuje jedną liczbę od drugiej """
    return X - Y

def mnozenie(X: float, Y: float) -> float:
    """ Mnoży jedną liczbe przez druga """
    return X * Y

def dzielenie(X: float, Y: float) -> float:
    """ Dzieli jedną liczbe przez drugą """
    return X / Y

print("Wybierz operację:")
print("1. Dodawanie")
print("2. Dzielenie")
print("3. Odejmowanie")
print("4. Mnożenie")

wybor = input("Proszę wybrać operację (1/2/3/4): ")

num_1 = None
num_2 = None

try:
    num_1 = float(input("Wpisz pierwszą liczbę: "))
    num_2 = float(input("Wpisz drugą liczbę: "))
except ValueError:
    print("Błąd: Wprowadzono niepoprawne dane. Wpisz liczby.")

if num_1 is not None and num_2 is not None:
    if wybor == '1':
        print(num_1, "+", num_2, "=", Dodawanie(num_1, num_2))
    elif wybor == '3':
        print(num_1, "-", num_2, "=", odejmowanie(num_1, num_2))
    elif wybor == '4':
        print(num_1, "*", num_2, "=", mnozenie(num_1, num_2))
    elif wybor == '2':
        if num_2 != 0:
            print(num_1, "/", num_2, "=", dzielenie(num_1, num_2))
        else:
            print("Błąd: Nie można dzielić przez zero.")
    else:
        print("To jest niepoprawne dane wejściowe.")

