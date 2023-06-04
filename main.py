import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import igraph as ig
from tqdm import tqdm

class MyGUI:


    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x300")
        self.root.title("ProgettoIUM Python")

        self.border_color = tk.Frame(self.root, background="red")

        self.label = tk.Label(self.root, text="Python GUI", font=('Helvetica Bold', 20))
        self.label.pack(padx=10, pady=10)

        self.label_word1 = tk.Label(self.root, text="Insert first word:", font=('Arial', 16))
        self.label_word1.pack(ipadx=3)

        self.textbox1 = tk.Entry(self.root, width=250, font=('Arial', 16))
        self.textbox1.pack(padx=10, pady=10)

        self.label_word2 = tk.Label(self.root, text="Insert second word:", font=('Arial', 16))
        self.label_word2.pack(ipadx=3)

        self.textbox2 = tk.Entry(self.root, width=400, font=('Arial', 16))
        self.textbox2.pack(padx=10, pady=10)

        self.label_attach_file_btn = tk.Label(self.root, text="Attach file to read:", font=('Arial', 16))
        self.label_attach_file_btn.pack(ipadx=3)

        self.attach_file_btn = tk.Button(self.root, text="Attach File", font=('Arial', 14), command=self.attach_file_to_read)
        self.attach_file_btn.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="INVIA", font=('Arial', 18), command=self.save_strings)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def save_strings(self):
        word1 = self.textbox1.get()
        word2 = self.textbox2.get()
        print("parola1 inserita: ", word1)
        print("parola2 inserita: ", word2)

    def attach_file_to_read(self):
        file_path = filedialog.askopenfilename(filetypes=[('Text file', '*.txt')])
        if file_path:
            with open(file_path, 'r') as file:
                words = file.read().split()
                return words

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit"):
            self.root.destroy()


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

gui = MyGUI()

words = gui.attach_file_to_read()
graph = ig.Graph(directed = True)


