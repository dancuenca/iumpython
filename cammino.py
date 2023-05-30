import random


def trova_cammino(parola_iniziale, parola_finale, dizionario):
    cammino = [parola_iniziale]  # Lista che conterrà il cammino tra le due parole

    while cammino[-1] != parola_finale:
        parola_corrente = cammino[-1]
        parole_vicine = [parola for parola in dizionario if
                         calculate_edit_distance(parola_corrente, parola) <= 2 and parola not in cammino]

        if not parole_vicine:
            # Non ci sono parole vicine non ancora visitate, il cammino non è possibile
            return None

        prossima_parola = random.choice(parole_vicine)
        cammino.append(prossima_parola)

    return cammino


def calculate_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Creazione di una matrice di dimensioni (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inizializzazione dei valori di base
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calcolo della distanza di modifica
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    return dp[m][n]

# Caricamento del dizionario di parole dal file di testo
try:
    with open("words.txt", "r") as file:
        dizionario = [parola.strip() for parola in file.readlines()]
except FileNotFoundError:
    print("File non trovato.")
    exit()

# Interazione con l'utente
parola_iniziale = input("Inserisci la parola iniziale: ")
parola_finale = input("Inserisci la parola finale: ")

cammino = trova_cammino(parola_iniziale, parola_finale, dizionario)

if cammino:
    print("Cammino trovato:")
    print(cammino)
else:
    print("Non è possibile trovare un cammino tra le due parole.")
