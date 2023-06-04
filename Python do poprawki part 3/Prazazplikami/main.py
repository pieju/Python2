import string

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_word_endings(text):
    words = text.split()
    endings = {}
    for word in words:
        # Usunięcie znaków interpunkcyjnych z końca słowa
        word = word.rstrip(string.punctuation)
        if word:
            ending = word[-1]
            if ending in endings:
                endings[ending] += 1
            else:
                endings[ending] = 1
    return endings

# Pobranie pliku tekstowego
with open('tekst.txt', 'r') as tekst:
    text = tekst.read()

# Obliczenie liczby słów
word_count = count_words(text)
print("Liczba słów:", word_count)

# Przygotowanie statystyk dotyczących końcówek słów
endings = get_word_endings(text)
print("Statystyki końcówek słów:")
for ending, count in endings.items():
    print(f"{ending}: {count}")

