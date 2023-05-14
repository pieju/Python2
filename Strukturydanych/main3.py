#zadanie3
mylist= ["burak","cukinia", "pomidor","cytryna", "ananas","papryka", "dynia"]
print("Podaj litere")
letter=input()
for element in mylist:
    if element.startswith(letter):
        print(element)