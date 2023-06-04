import json

class TodoList:
    def __init__(self):
        self.zadania = []
        self.wczytaj_zadania()

    def wczytaj_zadania(self):
        try:
            with open("zadania.json", "r") as plik:
                self.zadania = json.load(plik)
        except FileNotFoundError:
            self.zadania = []

    def zapisz_zadania(self):
        with open("zadania.json", "w") as plik:
            json.dump(self.zadania, plik)

    def wyswietl_zadania(self):
        if not self.zadania:
            print("Brak zapisanych zadań.")
        else:
            for zadanie in self.zadania:
                print(f"ID: {zadanie['id']}, Tytuł: {zadanie['tytuł']}, Termin: {zadanie['termin']}")

    def dodaj_zadanie(self):
        id_zadania = input("Podaj ID zadania")
        tytul = input("Podaj tytuł zadania: ")
        opis = input("Podaj opis zadania: ")
        termin = input("Podaj termin wykonania zadania: ")

        id_zadania = len(self.zadania) + 1

        zadanie = {
            "id": id_zadania,
            "tytuł": tytul,
            "opis": opis,
            "termin": termin
        }
        self.zadania.append(zadanie)
        self.zapisz_zadania()
        print("Zadanie dodane.")

    def usun_zadanie(self):
        id_zadania = int(input("Podaj ID zadania do usunięcia: "))

        for zadanie in self.zadania:
            if zadanie["id"] == id_zadania:
                self.zadania.remove(zadanie)
                self.zapisz_zadania()
                print("Zadanie usunięte.")
                return

        print("Nie znaleziono zadania o podanym ID.")

    def aktualizuj_zadanie(self):
        id_zadania = int(input("Podaj ID zadania do aktualizacji: "))

        for zadanie in self.zadania:
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

                self.zapisz_zadania()
                print("Zadanie zaktualizowane.")
                return

        print("Nie znaleziono zadania o podanym ID.")

    def zapisz_do_pliku(self):
        self.zapisz_zadania()
        print("Zadania zapisane do pliku.")

    def main(self):
        print("===== LISTA ZADAŃ =====")
        self.wyswietl_zadania()

        while True:
            print("\nOpcje:")
            print("1. Dodaj zadanie")
            print("2. Usuń zadanie")
            print("3. Aktualizuj zadanie")
            print("4. Zapisz zadania do pliku")
            print("5. Wyjdź z programu")

            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                self.dodaj_zadanie()
            elif wybor == "2":
                self.usun_zadanie()
            elif wybor == "3":
                self.aktualizuj_zadanie()
            elif wybor == "4":
                self.zapisz_do_pliku()
            elif wybor == "5":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

        print("Do widzenia!")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.main()
