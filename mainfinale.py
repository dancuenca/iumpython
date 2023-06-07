import igraph as ig
from tqdm import tqdm
import time

def rem(string, index):
    return string[:index] + string[index+1:]

def addLetter(string,char,index):
    return string[:index] + char + string[index:]


def sub(string,oldchar_index,newchar):
    return string[:oldchar_index] + newchar + string[oldchar_index+1:]

def links(words,word):
    a = 'abcdefghijklmnopqrstuwxyz'
    edges = []
    costs = []
    ops = []
    for index in range(len(word)):
        for letter in a:
            newWord = addLetter(word, letter, index)
            if newWord in words:
                edges.append((word,newWord))
                costs.append(2)
                ops.append("add")
            newWord = sub(word,index,letter)
            if newWord in words:
                edges.append((word,newWord))
                costs.append(3)
                ops.append("sub")
            newWord = rem(word, index)
            if newWord in words:
                edges.append((word,newWord))
                costs.append(2)
                ops.append("rem")
    return edges, costs, ops


def printPath(word1,word2):
    val = graph.get_shortest_paths(word1,word2,costs,"out","epath")
    val1 = graph.get_shortest_paths(word1,word2,costs,"out","vpath")
    val = val[0]
    val1 = val1[0]
    stringa = ""
    for cnt in range(int(len(val1))):
        if cnt<int(len(val)):
            stringa = stringa + graph.vs[val1[cnt]]["name"]+"-"+graph.es[val[cnt]]["name"]+"->"
        else:
            stringa = stringa + graph.vs[val1[cnt]]["name"]
    print(stringa+" "+str(graph.distances(word1,word2,costs,"out")[0][0]))


words = set()
graph = ig.Graph(directed = True)
f = open('words.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    word = line.strip()
    words.add(word)
f.close()
graph.add_vertices(list(words))
edges = []
costs = []
ops = []
with tqdm(total=len(words)) as pbar:
    for word in words:
        el = links(words=words,word=word)
        edges += el[0]
        costs += el[1]
        ops += el[2]
        pbar.update(1)
graph.add_edges(edges)
graph.es["name"] = ops
word1 = str(input("prima parola: "))
word2 = str(input("seconda parola: "))
printPath(word1,word2)