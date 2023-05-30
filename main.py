import collections
import itertools

def create_graph(words):
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

    graph = collections.defaultdict(set)
    for word in words:
        word = word.lower()
        for neigh in neighbors(word):
            if neigh in words:
                graph[word].add(neigh)
        for anagram in anagrams(word):
            if anagram in words and anagram != word:
                graph[word].add(anagram)
    return graph

def shortest_path(graph, start, end):
    queue = collections.deque([[start]])
    seen = set([start])

    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield path
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(path + [neighbor])

words = ['casa', 'casta', 'costa', 'costo', 'cosmo']  # Lista delle parole
graph = create_graph(words)
path_generator = shortest_path(graph, 'casa', 'cosmo')

for path in path_generator:
    if path[-1] == 'cosmo':
        print(' -> '.join(path))
        break