from collections import deque

def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [word.strip() for word in file]

def find_word_path(word1, word2, dictionary):
    # Funzione per controllare se due parole differiscono per una singola lettera
    def differ_by_single_letter(word1, word2):
        if len(word1) != len(word2):
            return False
        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1
        return diff_count == 1

    # Funzione per generare le parole che differiscono per una singola lettera
    def generate_single_letter_diff_words(word):
        diff_words = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(word)):
            for letter in alphabet:
                new_word = word[:i] + letter + word[i + 1:]
                if new_word in dictionary and new_word != word:
                    diff_words.append(new_word)
        return diff_words

    # Algoritmo di ricerca in ampiezza per trovare il percorso tra le parole
    queue = deque()
    queue.append((word1, [word1]))  # Coda con elementi (parola, percorso)
    visited = set([word1])  # Insieme delle parole visitate

    while queue:
        current_word, current_path = queue.popleft()

        if current_word == word2:
            return current_path  # Ritorna il percorso se si raggiunge la parola di destinazione

        # Genera le parole vicine che differiscono per una singola lettera
        next_words = generate_single_letter_diff_words(current_word)

        for next_word in next_words:
            if next_word not in visited:
                queue.append((next_word, current_path + [next_word]))
                visited.add(next_word)

    return []  # Se non viene trovato alcun percorso

# Esempio di utilizzo
dictionary = load_dictionary('words.txt')

input_word1 = input("Inserisci la prima parola: ")
input_word2 = input("Inserisci la seconda parola: ")

word_path = find_word_path(input_word1, input_word2, dictionary)

if word_path:
    print("Percorso tra le parole:")
    print(" -> ".join(word_path))
else:
    print("Nessun percorso trovato.")