# 📦 Barcode Generator (Day 01)
# This is a simple Python GUI app that generates a random barcode (Code128)
# and saves it as a PNG image file when you click a button.

import tkinter as tk  
from tkinter import messagebox  # Used for building the graphical interface (GUI)
import random                          # Used to generate a random string for the barcode
import barcode                         # The library that actually creates the barcode
from barcode.writer import ImageWriter  # Allows us to save the barcode as a PNG image
from PIL import Image, ImageTk         # (Optional) for image handling – not used here but can be helpful for previews

# This function gets triggered when the user clicks the "Generate Barcode" button
def create_barcode():
    # Create a random 8-character alphanumeric string (e.g., 4GJ9W2KD)
    value = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

    # Generate the barcode in Code128 format
    code128 = barcode.get('code128', value, writer=ImageWriter())

    # Save the barcode to a file like "barcode_4GJ9W2KD.png"
    filename = f"barcode_{value}"
    code128.save(filename)

    # Show a popup to confirm it worked
    msg = f"✅ Barcode Created!\n\nSaved as: {filename}.png"
    messagebox.showinfo("Success", msg)

# ----- GUI Setup -----

# Create the main window
root = tk.Tk()
root.title("Barcode Generator")  # Set window title
root.geometry("300x150")         # Set window size

# Create a frame to hold the button
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Add a label at the top of the window
label = tk.Label(frame, text="Click to generate a random barcode", font=("Arial", 10))
label.pack(pady=(0, 10))

# Add a button that runs create_barcode() when clicked
button = tk.Button(frame, text="Generate Barcode", command=create_barcode, bg="lightblue", font=("Arial", 10, "bold"))
button.pack()

# Start the GUI application (keep the window open)
root.mainloop()
