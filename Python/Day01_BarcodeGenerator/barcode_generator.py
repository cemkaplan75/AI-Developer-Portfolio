import tkinter as tk
from tkinter import messagebox
import random
import string
import barcode
from barcode.writer import ImageWriter
import os

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_barcode():
    random_code = generate_random_string()
    code128 = barcode.get('code128', random_code, writer=ImageWriter())
    filename = f"barcode_{random_code}"
    file_path = code128.save(filename)
    messagebox.showinfo("Barcode Created", f"Saved as: {file_path}")

root = tk.Tk()
root.title("Barcode Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Click to generate a random barcode")
label.pack(pady=10)

button = tk.Button(frame, text="Generate Barcode", command=create_barcode)
button.pack()

root.mainloop()
