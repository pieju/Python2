class Czytelnik:
    def __init__(self, imie, nazwisko, numer_karty,book):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_karty = numer_karty
        self.book = book
    
    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko} i czytam książke {self.book}")


czytelnik1 = Czytelnik("Asia", "Jendrych", "123456", "Szklany Tron")
czytelnik2 = Czytelnik("Cassian", "Cytrynka", "987654", "Trening Funkcjonalny")
czytelnik3 = Czytelnik("Julia", "Gorzka", "7896765","Zmierzch")


czytelnik1.przedstaw_sie()
czytelnik2.przedstaw_sie()
czytelnik3.przedstaw_sie()