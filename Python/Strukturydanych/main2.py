#zadanie2
slowo = input("Podaj slowo: ")


odwrocone_slowo = ""
for index in range(len(slowo)-1, -1, -1):
    odwrocone_slowo += slowo[index]

if odwrocone_slowo == slowo:
    print("Palindrom")
else:
    print("Podane slowo nie jest palindronem")