#zadanie 1
liczba = (10, -3, 4, 9, 12, -6, 0)
max_num = liczba[0]
min_num = liczba[0]
for num in liczba:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"Największa liczba to: {max_num}")
print(f"Najmniejsza liczba to: {min_num}")
