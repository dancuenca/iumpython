from collections import deque


def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return set(words)


def get_adjacent_words(word, dictionary):
    adjacent_words = []
    for i in range(len(word)):
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            new_word = word[:i] + letter + word[i+1:]
            if new_word != word and new_word in dictionary:
                adjacent_words.append(new_word)
    return adjacent_words


def build_word_path(start_word, end_word, dictionary):
    queue = deque([(start_word, [start_word])])
    visited = set()

    while queue:
        word, path = queue.popleft()

        if word == end_word:
            return path

        if word not in visited:
            visited.add(word)
            adjacent_words = get_adjacent_words(word, dictionary)
            for adjacent_word in adjacent_words:
                if adjacent_word not in visited:
                    queue.append((adjacent_word, path + [adjacent_word]))

    return None


# Carica il dizionario di parole
dictionary_file = 'words.txt'  # Inserisci il percorso corretto al tuo file dizionario
dictionary = load_dictionary(dictionary_file)

# Richiedi all'utente di inserire due parole
start_word = input("Inserisci la parola di partenza: ")
end_word = input("Inserisci la parola di destinazione: ")

# Costruisci il cammino tra le due parole
path = build_word_path(start_word, end_word, dictionary)

# Stampa il risultato
if path:
    print(f"\nCammino tra '{start_word}' e '{end_word}':")
    for word in path:
        print(word)
else:
    print(f"Non esiste un cammino tra '{start_word}' e '{end_word}'.")
