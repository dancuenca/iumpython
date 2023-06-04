import tkinter as tk

def mostra_contenuto_array(array):
    root = tk.Tk()
    root.title("Contenuto dell'array")

    # Creazione di un widget Label per visualizzare il contenuto dell'array
    label = tk.Label(root, text="\n".join(array))
    label.pack()

    root.mainloop()

# Esempio di utilizzo
array = ['Elemento 1', 'Elemento 2', 'Elemento 3']
mostra_contenuto_array(array)