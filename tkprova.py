import tkinter as tk

# Creazione di una finestra principale
window = tk.Tk()

# Aggiunta di un titolo alla finestra
window.title("La mia finestra")

# Creazione di un'etichetta nella finestra
label = tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()

# Esecuzione del ciclo principale dell'interfaccia grafica
window.mainloop()