# 📦 Day 01: Barcode Generator

This project is a simple **Python GUI application** that generates random **Code128 barcodes** and saves them as PNG image files.

It is designed as part of a daily portfolio project to showcase hands-on coding, GUI development, and image generation with Python.

---

## 🚀 Features

- Graphical User Interface (GUI) built with `tkinter`
- Random alphanumeric string generation using Python's `random` module
- Barcode creation using the `python-barcode` library
- Image rendering and saving with `pillow`
- One-click barcode generation
- Saves barcode as `.png` in the local folder

---

## 🧰 Technologies Used

| Purpose                | Library            |
|------------------------|--------------------|
| GUI creation           | `tkinter` (built-in) |
| Barcode generation     | `python-barcode`   |
| Image rendering (PNG)  | `pillow` (PIL)     |
| Random string creation | `random` (built-in)|

---

## 🧠 How It Works

1. A GUI window is created using `tkinter`, with a button labeled **"Generate Barcode"**.
2. When the button is clicked:
   - A random 8-character alphanumeric string is generated.
   - A Code128 barcode is created using that string.
   - The barcode is rendered as a `.png` file using `pillow`.
   - The file is saved with the name `barcode_<RANDOM>.png`.

---

## 📸 Sample Output

The image below is a **real barcode** created by this application:

![Generated Barcode](barcode_D9DK9UWF.png)

> ✅ This confirms that the code successfully generates, renders, and saves a valid barcode image.

---

## 📦 Install Dependencies

Before running the app, make sure to install the required libraries:

```bash
pip install python-barcode pillow
