import networkx as nx
import heapq

def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    return dp[m][n]

def calculate_edit_distance(filename):
    with open(filename, 'r') as file:
        words = file.read().split()

    results = []

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            distance = edit_distance(word1, word2)
            results.append((word1, word2, distance))

    return results

def create_graph_from_sorted_results(sorted_results):
    graph = nx.Graph()

    for word1, word2, distance in sorted_results:
        graph.add_edge(word1, word2, weight=distance)

    return graph

def shortest_path(graph, start_node, end_node):
    visited = {start_node}

    priority_queue = [(0, start_node)]

    print("nodo di partenza: ", start_node)

    while priority_queue:
        print("dentro while")
        print("CODA DI PRIORITA: ", priority_queue)
        current_weight, current_node = heapq.heappop(priority_queue)

        print("nodo corrente: ", current_node, " , peso: ", current_weight)

        # controllo se si è raggiunto il nodo di destinazione
        if current_node == end_node:
            break

        # controllo dei nodi vicini
        for neighbor, edge_attrs in graph[current_node].items():
            print("dentro for")
            weight = edge_attrs['weight']

            print("vicino nodo corrente: ", neighbor, ", peso: ", weight)

            if neighbor not in visited:
                heapq.heappush(priority_queue, (weight, neighbor))
                print("aggiungo a coda e nei nodi visitati: ", neighbor)
                visited.add(neighbor)
            else:
                print("nodo già visitato")

        print("--> fine visita dei vicini di: ", current_node)
        print("NODI VISITATI: ", visited)

    # Costruzione dell'array dei nodi visitati
    visited_nodes = list(visited)

    return visited_nodes


filename = 'words.txt'
results = calculate_edit_distance(filename)

sorted_results = sorted(results, key=lambda x: x[2])

graph = create_graph_from_sorted_results(sorted_results)

#print("\nedit distance ordinata: ")

#for word1, word2, distance in sorted_results:
#    print(f"Distanza tra {word1} e {word2}: {distance}")

#print("\n")
#print("Nodi del grafo:", graph.nodes())

#for node1, node2, attrs in graph.edges(data=True):
#    weight = attrs['weight']
#    print(f"Arco tra {node1} e {node2}, peso: {weight}")

#print("\n\n")

start_node = "casa"
end_node = "cosmo"
path = shortest_path(graph, start_node, end_node)

print(path)




