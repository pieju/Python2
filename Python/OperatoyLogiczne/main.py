print("Podaj swój wiek")
age = int(input())
print("Masz prawo jazdy kat. A2? Tak lub nie.")
anserw= input()
if anserw == 'tak':
    print("Ile lat je posiadasz")
    liczba=int(input())
if age >= 24 or (anserw and age>=20 and liczba >= 2):
    print("Możesz przystąpić do egzaminu na prawo jazdy kat. A")
else:
    print("Nie mozesz przystapic do egzainu na prawo jazdy kat. A")