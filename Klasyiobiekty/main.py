class Czytelnik:
    def __init__(self,name,surname,email,book) -> None:
        self.name=name
        self.surname=surname
        self.email=email
        self.book=book
        
        
    def __str__(self):
        return ({self.name},{self.surname}, {self.email}, {self.book})

C1 = Czytelnik("Asia", "Jendrych", "j.jendrychak@gmail.com","Szklany Tron")
C2 = Czytelnik("Julia", "Gorzkiewicz", "j.gorzkiewicz@gmail.com","Zmierzch")
C3 = Czytelnik("Julia", "Pietrak", "julia.pietrak@gmail.com","Szeptem")

print(C1.__str__())
print(C2.__str__())
print(C3.__str__())