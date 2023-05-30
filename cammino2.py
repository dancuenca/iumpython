from collections import deque

def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Creazione della matrice per il calcolo delle distanze
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inizializzazione dei valori base
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calcolo dell'edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]


def build_graph(filename):
    graph = {}

    with open(filename, 'r') as file:
        words = file.read().split()

    for i in range(len(words)):
        word = words[i]
        if word not in graph:
            graph[word] = []

        for j in range(i + 1, len(words)):
            other_word = words[j]
            edit_dist = edit_distance(word, other_word)

            # Aggiungiamo un peso inversamente proporzionale all'edit distance
            weight = 1.0 / (edit_dist + 1)

            graph[word].append((other_word, weight))
            graph[other_word].append((word, weight))

    return graph


# Esempio di utilizzo
filename = 'words.txt'  # Inserisci il nome del tuo file di testo

graph = build_graph(filename)

# Stampa il grafo
for word, edges in graph.items():
    print(f"{word}: {edges}")
