import igraph as ig
from tqdm import tqdm
import tkinter as tk

def salva_stringa():
    global stringa_salvata1
    global stringa_salvata2
    stringa_salvata1 = entry.get()  # Ottieni il testo dalla casella di testo
    stringa_salvata2 = entry2.get()

# Creazione della finestra
finestra = tk.Tk()
finestra.title("Salva stringa")

# Creazione della casella di testo
entry = tk.Entry(finestra, width=30)
entry.pack()

salva_button = tk.Button(finestra, text="Salva", command=salva_stringa)
salva_button.pack()

entry2 = tk.Entry(finestra, width=30)
entry2.pack()

# Creazione del pulsante di salvataggio
salva_button2 = tk.Button(finestra, text="Salva", command=salva_stringa)
salva_button2.pack()

# Variabile per salvare la stringa
stringa_salvata1 = ""
stringa_salvata2 = ""

print("Stringa1 salvata:", stringa_salvata1)
print("Stringa2 salvata:", stringa_salvata2)

# Avvio dell'interfaccia grafica
finestra.mainloop()

# Stampa della stringa salvata
print("Stringa1 salvata:", stringa_salvata1)
print("Stringa2 salvata:", stringa_salvata2)
