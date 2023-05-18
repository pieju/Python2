from calc import *
print("Wybierz operacje:")
print("1. Dodawanie")
print("2. Dzielenie")
print("3. Odejmowanie")
print("4. Mnozenie")


wybor = input("Prosze wybrac operacje (1/2/3/4):")

num_1= float(input("Wpisz pierwsza liczbe"))
num_2 = float(input("Wpisz druga liczbe"))

if wybor == '1':
    print(num_1,"+", num_2, "=", Dodawanie(num_1,num_2))

elif wybor == '3':
    print(num_1,"-", num_2, "=", odejmowanie(num_1,num_2))

elif wybor == '4':
    print(num_1,"*", num_2, "=", mnozenie (num_1,num_2))
elif wybor == '2':
    print(num_1,"/", num_2, "=", dzielenie(num_1,num_2))

else:  
    print("To jest niepoprawny input")

