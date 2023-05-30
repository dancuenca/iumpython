import collections
import itertools

def create_graph(file_name):
    def neighbors(word):
        for i in range(len(word)):
            yield word[:i] + word[i+1:]  # Rimuovere una lettera
            for c in 'abcdefghijklmnopqrstuvwxyz':
                yield word[:i] + c + word[i:]  # Aggiungere una lettera
                yield word[:i] + c + word[i+1:]  # Cambiare una lettera
        for c in 'abcdefghijklmnopqrstuvwxyz':
            yield word + c  # Aggiungere una lettera alla fine

    def anagrams(word):
        return ("".join(perm) for perm in itertools.permutations(word))

    words = set()
    with open(file_name, 'r') as file:
        for line in file:
            word = line.strip().lower()
            words.add(word)

    graph = collections.defaultdict(set)
    for word in words:
        for neigh in neighbors(word):
            if neigh in words:
                graph[word].add(neigh)
        for anagram in anagrams(word):
            if anagram in words and anagram != word:
                graph[word].add(anagram)
    return graph

graph = create_graph('words.txt')  # 'words.txt' è il file da cui si leggono le parole
print(graph)  # Stampa il grafo