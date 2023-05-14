import random
from typing import List, Set

# wczytanie list imion i nazwisk
with open('imiona.txt', encoding='utf-8') as f:
    imiona: List[str] = [line.strip() for line in f]

with open('nazwiska.txt', encoding='utf-8') as f:
    nazwiska: List[str] = [line.strip() for line in f]

# pobranie liczby kombinacji od użytkownika
liczba_kombinacji: int = int(input('Podaj liczbę kombinacji: '))

# wygenerowanie losowych kombinacji imion i nazwisk
kombinacje: Set[str] = set()
while len(kombinacje) < liczba_kombinacji:
    imie: str = random.choice(imiona)
    nazwisko: str = random.choice(nazwiska)
    kombinacja: str = f'{imie} {nazwisko}'
    kombinacje.add(kombinacja)

# zapisanie kombinacji do pliku
with open('kombinacje.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(kombinacje))