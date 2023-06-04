import customtkinter
from customtkinter import filedialog
import igraph as ig

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x450")
file_path = ""


def attach_file_to_read():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Text file', '*.txt')])


def add(string, char, index):
    return string[:index] + char + string[index:]


def substitute(string, oldchar_index, newchar):
    return string[:oldchar_index] + newchar + string[oldchar_index+1:]


def remove(string, index):
    return string[:index] + string[index + 1:]


def links(words, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    edges = []
    costs = []
    operations = []

    for index in range(len(word)):
        for letter in alphabet:
            new_word = add(word, letter, index)
            if new_word in words:
                edges.append(words, word)
                costs.append(2)
                operations.append("add")
            new_word = substitute(word, index, letter)
            if new_word in words:
                edges.append(words, word)
                costs.append(3)
                operations.append("sub")
            new_word = remove(word, index)
            if new_word in words:
                edges.append(words, word)
                costs.append(2)
                operations.append("rem")

    return edges, costs, operations


def print_path(word1, word2, costs):
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

def run_program():
    word1 = entry1.get()
    word2 = entry2.get()
    global file_path
    if file_path:
        with open(file_path, 'r') as file:
            words = file.read().split()

    print("word1: ", word1)
    print("word2: ", word2)
    print("file letto: ", words)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Python GUI", font=('Roboto', 24))
label.pack(pady=12, padx=10)

label_entry1 = customtkinter.CTkLabel(master=frame, text="Insert first word:", font=('Roboto', 14))
label_entry1.pack()

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="First word", width=300)
entry1.pack(pady=12, padx=10)

label_entry2 = customtkinter.CTkLabel(master=frame, text="Insert second word:", font=('Roboto', 14))
label_entry2.pack()

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Second word", width=300)
entry2.pack(pady=12, padx=10)

label_attach_file_btn = customtkinter.CTkLabel(master=frame, text="Attach file to read:", font=('Roboto', 14))
label_attach_file_btn.pack()

attach_file_btn = customtkinter.CTkButton(master=frame, text="Attach File", font=('Arial', 14), command=attach_file_to_read)
attach_file_btn.pack(padx=10, pady=10)

button = customtkinter.CTkButton(master=frame, text="SEND", font=('Roboto', 20), command=run_program)
button.pack(pady=20, padx=10)

graph = ig.Graph(directed = True)

root.mainloop()