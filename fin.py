import tkinter
import customtkinter
from customtkinter import filedialog
import igraph as ig

# Functions for GUI
file_path = ""

def attach_file_to_read():
    global file_path
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Text file', '*.txt')])
        state_attaching_label.configure(text="Attached file: "+ file_path.title(), text_color="green")
    except:
        state_attaching_label.configure(text="File attached is not valid!", text_color="red")

def run_program():
    print("word1: ", entry_word1.get())
    print("word2: ", entry_word2.get())

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

# File attaching success/fail
state_attaching_label = customtkinter.CTkLabel(app, text="")
state_attaching_label.pack()

# Send button
send_button = customtkinter.CTkButton(app, text="SEND", font=('Roboto', 20), command=run_program)
send_button.pack(pady=20, padx=10)

# Run App
app.mainloop()