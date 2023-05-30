import networkx as nx

def build_graph(file_path):
    # Creazione di un grafo vuoto
    graph = nx.Graph()

    # Apertura del file di testo in modalità lettura
    with open(file_path, 'r') as file:
        # Lettura delle parole dal file riga per riga
        for line in file:
            # Rimozione dei caratteri di spazio e separazione delle parole
            words = line.strip().split()

            # Aggiunta delle parole come nodi del grafo
            for word in words:
                graph.add_node(word)

            # Aggiunta degli archi tra le parole adiacenti
            for i in range(len(words) - 1):
                graph.add_edge(words[i], words[i + 1])

    return graph

# Esempio di utilizzo
file_path = 'words.txt'  # Inserisci il percorso del tuo file di testo
graph = build_graph(file_path)

# Stampa dei nodi e degli archi del grafo
print("Nodi del grafo:", graph.nodes())
print("Archi del grafo:", graph.edges())
