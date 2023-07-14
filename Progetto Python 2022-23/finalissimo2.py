import customtkinter
from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog
import igraph as ig

# Functions for data elaborations
def add(string, char, index):
    return string[:index] + char + string[index:]


def substitute(string, oldchar_index, newchar):
    return string[:oldchar_index] + newchar + string[oldchar_index+1:]


def remove(string, index):
    return string[:index] + string[index+1:]


def links(words, word):
    alphabet = 'abcdefghijklmnopqrstuwxyz'
    edges = []
    costs = []
    operations = []
    for index in range(len(word)):
        for letter in alphabet:
            new_word = add(word, letter, index)
            if new_word in words:
                edges.append((word, new_word))
                costs.append(2)
                operations.append("addition")
            new_word = substitute(word, index, letter)
            if new_word in words:
                edges.append((word, new_word))
                costs.append(3)
                operations.append("replacement")
            new_word = remove(word, index)
            if new_word in words:
                edges.append((word, new_word))
                costs.append(2)
                operations.append("removal")
    return edges, costs, operations


# Functions for GUI
file_path = ""
res = ""


def print_path(graph, costs, word1, word2):
    result_path = []
    global res

    try:
        val = graph.get_shortest_paths(word1, word2, costs, "out", "epath")
        val1 = graph.get_shortest_paths(word1, word2, costs, "out", "vpath")
    except:
        progressbar_label.configure(text="Words entered are not contained in the attached file!", text_color="red")

    val = val[0]
    val1 = val1[0]
    temp = ""
    for cnt in range(int(len(val1))):
        if cnt < int(len(val)):
            temp += graph.vs[val1[cnt]]["name"]+"\n-> "+graph.es[val[cnt]]["name"]+"\n"
        else:
            temp += graph.vs[val1[cnt]]["name"]

    res = temp + "\nRules weight: " + str(graph.distances(word1, word2, costs, "out")[0][0])
    return res


def attach_file_to_read():
    global file_path
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Text file', '*.txt')])
        state_attaching_label.configure(text="Attached file: " + file_path.title(), text_color="green")
    except:
        state_attaching_label.configure(text="File attached is not valid!", text_color="red")

    words = read_file()

    progressbar_label.pack(padx=10)
    progress_bar.pack(pady=20)
    app.update()

    # Create graph
    global graph
    global edges
    global costs
    global operations
    graph = ig.Graph(directed=True)
    graph.add_vertices(list(words))
    edges = []
    costs = []
    operations = []

    update_interval = int(len(words) / 10)
    index = 1

    for word in words:
        el = links(words, word)
        edges += el[0]
        costs += el[1]
        operations += el[2]
        index += 1

        if index % update_interval == 0:
            progress_bar.set(index / len(words))
            app.update()

    progressbar_label.configure(text="Done!", text_color="green", font=('Roboto', 20))
    progress_bar.pack_forget()

    graph.add_edges(edges)
    graph.es["name"] = operations


# Read attached file and save it in array
def read_file():
    words = set()
    try:
        f = open(file_path, 'r')
        while True:
            line = f.readline()
            if not line:
                break
            word = line.strip()
            words.add(word)
        f.close()
    except:
        progressbar_label.configure(text="File attached is not valid!", text_color="red")
    return words


def is_words_in_array(word1, word2, words):
    words_set = set(words)
    return word1 in words_set and word2 in words_set


def run_program():
    # Save inputs in variable
    word1 = entry_word1.get()
    word2 = entry_word2.get()

    # Print path from word1 to word2
    final_result = print_path(graph, costs, word1, word2)

    CTkMessagebox(app, title="Result", message=final_result, icon="check")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("820x580")
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

# Progress bar
progress_bar = customtkinter.CTkProgressBar(app, width=300, mode="determinate")
progress_bar.set(0)

# Final output Result
result = customtkinter.CTkLabel(app, text=res, font=('Roboto', 20))

# Run App
app.mainloop()