import tkinter as tk
from tkinter import messagebox
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

        self.button = tk.Button(self.root, text="INVIA", font=('Arial', 18), command=self.save_strings)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

        self.root.mainloop()

    def save_strings(self):
        word1 = self.textbox1.get()
        word2 = self.textbox2.get()
        print("parola1 inserita: ", word1)
        print("parola2 inserita: ", word2)

    def remove(string, index):
        #rimuove il carattere in posizione index della stringa e restituisce una nuova stringa senza il carattere rimosso
        return string[:index] + string[index+1:]

    def add(string, character, index):
        return string[:index] + character + string[index:]

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit"):
            self.root.destroy()

MyGUI()

