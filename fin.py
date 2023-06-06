import tkinter
import customtkinter
from customtkinter import filedialog
import igraph as ig
from tqdm import tqdm

# Functions for data elaborations
def add(string, char, index):
    return string[:index] + char + string[index:]

def substitute(string, oldchar_index, newchar):
    return string[:oldchar_index] + newchar + string[oldchar_index+1:]

def remove(string, index):
    return string[:index] + string[index+1:]

def links(words,word):
    a = 'abcdefghijklmnopqrstuwxyz'
    edges = []
    costs = []
    ops = []
    for index in range(len(word)):
        for letter in a:
            newWord = add(word, letter, index)
            if newWord in words:
                edges.append((word,newWord))
                costs.append(2)
                ops.append("add")
            newWord = substitute(word,index,letter)
            if newWord in words:
                edges.append((word,newWord))
                costs.append(3)
                ops.append("sub")
            newWord = remove(word, index)
            if newWord in words:
                edges.append((word,newWord))
                costs.append(2)
                ops.append("rem")
    return edges, costs, ops


def print_path(graph, costs, word1, word2):
    val = graph.get_shortest_paths(word1, word2, costs, "out", "epath")
    val1 = graph.get_shortest_paths(word1, word2, costs, "out", "vpath")
    val = val[0]
    val1 = val1[0]
    stringa = ""
    for cnt in range(int(len(val1))):
        if cnt < int(len(val)):
            stringa = stringa + graph.vs[val1[cnt]]["name"]+"-"+graph.es[val[cnt]]["name"]+"->"
        else:
            stringa = stringa + graph.vs[val1[cnt]]["name"]
    print(stringa+" "+str(graph.distances(word1, word2, costs, "out")[0][0]))


# Functions for GUI
file_path = ""

def attach_file_to_read():
    global file_path
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Text file', '*.txt')])
        state_attaching_label.configure(text="Attached file: "+ file_path.title(), text_color="green")
    except:
        state_attaching_label.configure(text="File attached is not valid!", text_color="red")

# Read attached file and save it in array
#def read_file():
#    words = set()
#    f = open(file_path, 'r')
#    progressbar_label.pack(padx=10)
#    progressbar.pack(padx=20)
#    progressbar.start()
#    while True:
#        line = f.readline()
#        if not line:
#            break
#        word = line.strip()
#        words.add(word)
#    f.close()
#    progressbar.stop()
#    progressbar.pack_forget()
#    return words

#def create_graph(words):
#    graph = ig.Graph(directed = True)
#    graph.add_vertices(list(words))
#    edges = []
#    costs = []
#    operations = []

#    for word in words:
#        element = links(words, word)
#        edges += element[0]
#        costs += element[1]
#        operations += element[2]

#    graph.add_edges(edges)
#    graph.es["name"] = operations

#    return graph

def run_program():
    print("word1: ", entry_word1.get())
    print("word2: ", entry_word2.get())
    word1 = entry_word1.get()
    word2 = entry_word2.get()
    words = set()
    f = open(file_path, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        word = line.strip()
        words.add(word)
    f.close()
    graph = ig.Graph(directed = True)
    graph.add_vertices(list(words))
    edges = []
    costs = []
    operations = []
    with tqdm(total=len(words)) as pbar:
        for word in words:
            el = links(words, word)
            edges += el[0]
            costs += el[1]
            operations += el[2]
            pbar.update(1)
    graph.add_edges(edges)
    graph.es["name"] = operations
    print_path(graph, costs, word1, word2)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Progetto IUM Python-GUI")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Python GUI", font=('Roboto', 24))
title.pack(pady=12, padx=10)

# Input word1
label_word1 = customtkinter.CTkLabel(app, text="Insert first word:", font=('Roboto', 14))
label_word1.pack()
entry_word1 = customtkinter.CTkEntry(app, placeholder_text="First word", width=300)
entry_word1.pack(pady=12, padx=10)

# Input word2
label_word2 = customtkinter.CTkLabel(app, text="Insert second word:", font=('Roboto', 14))
label_word2.pack()
entry_word2 = customtkinter.CTkEntry(app, placeholder_text="Second word", width=300)
entry_word2.pack(pady=12, padx=10)

# Attach file button
label_attach_file_btn = customtkinter.CTkLabel(app, text="Attach file to read:", font=('Roboto', 14))
label_attach_file_btn.pack()

attach_file_btn = customtkinter.CTkButton(app, text="Attach File", font=('Arial', 14), command=attach_file_to_read)
attach_file_btn.pack(padx=10, pady=10)

# File attaching success/fail label
state_attaching_label = customtkinter.CTkLabel(app, text="")
state_attaching_label.pack()

# Send button
send_button = customtkinter.CTkButton(app, text="SEND", font=('Roboto', 20), command=run_program)
send_button.pack(pady=20, padx=10)

# Label "loading" for progress bar
progressbar_label = customtkinter.CTkLabel(app, text="Loading...", font=('Roboto', 12))
#progressbar_label.pack(padx=10)

# Progress bar (initially invisible)
progressbar = customtkinter.CTkProgressBar(app)
#progressbar.pack(padx=20)

# Run App
app.mainloop()