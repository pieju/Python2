import json

zadania = []

def wczytaj_zadania():
    try:
        with open("zadania.json", "r") as plik:
            zadania.extend(json.load(plik))
    except FileNotFoundError:
        zadania.clear()

def zapisz_zadania():
    with open("zadania.json", "w") as plik:
        json.dump(zadania, plik)

def wyswietl_zadania():
    if not zadania:
        print("Brak zapisanych zadań.")
    else:
        for zadanie in zadania:
            print(f"ID: {zadanie['id']}, Tytuł: {zadanie['tytuł']}, Termin: {zadanie['termin']}")

def dodaj_zadanie():
    tytul = input("Podaj tytuł zadania: ")
    opis = input("Podaj opis zadania: ")
    termin = input("Podaj termin wykonania zadania: ")

    id_zadania = len(zadania) + 1

    zadanie = {
        "id": id_zadania,
        "tytuł": tytul,
        "opis": opis,
        "termin": termin
    }
    zadania.append(zadanie)
    zapisz_zadania()
    print("Zadanie dodane.")

def usun_zadanie():
    id_zadania = int(input("Podaj ID zadania do usunięcia: "))

    for zadanie in zadania:
        if zadanie["id"] == id_zadania:
            zadania.remove(zadanie)
            zapisz_zadania()
            print("Zadanie usunięte.")
            return

    print("Nie znaleziono zadania o podanym ID.")

def aktualizuj_zadanie():
    id_zadania = int(input("Podaj ID zadania do aktualizacji: "))

    for zadanie in zadania:
        if zadanie["id"] == id_zadania:
            tytul = input("Podaj nowy tytuł zadania (naciśnij Enter, aby pominąć): ")
            if tytul:
                zadanie["tytuł"] = tytul

            opis = input("Podaj nowy opis zadania (naciśnij Enter, aby pominąć): ")
            if opis:
                zadanie["opis"] = opis

            termin = input("Podaj nowy termin wykonania zadania (naciśnij Enter, aby pominąć): ")
            if termin:
                zadanie["termin"] = termin

            zapisz_zadania()
            print("Zadanie zaktualizowane.")
            return

    print("Nie znaleziono zadania o podanym ID.")

def main():
    wczytaj_zadania()
    print("===== LISTA ZADAŃ =====")

    while True:
        print("\nOpcje:")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Aktualizuj zadanie")
        print("5. Zapisz zadania do pliku")
        print("6. Wyjdź z programu")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            wyswietl_zadania()
        elif wybor == "2":
            dodaj_zadanie()
        elif wybor == "3":
            usun_zadanie()
        elif wybor == "4":
            aktualizuj_zadanie()
        elif wybor == "5":
            zapisz_zadania()
            print("Zadania zapisane do pliku.")
        elif wybor == "6":
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

    print("Do widzenia!")

if __name__ == "__main__":
    main()