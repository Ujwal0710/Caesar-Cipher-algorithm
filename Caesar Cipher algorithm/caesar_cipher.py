import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = ''
    if not -26 < shift < 26:
        shift = shift % 26

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

def process_text():
    text = text_entry.get()
    shift = int(shift_entry.get())
    mode = mode_combo.get().lower()

    if mode not in ['encrypt', 'decrypt']:
        result_label.config(text="Invalid mode. Please select 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(text, shift, mode)
    result_label.config(text="Result: " + result)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher")

# Text input
text_label = ttk.Label(root, text="Enter text:")
text_label.pack(pady=5)
text_entry = ttk.Entry(root, width=50)
text_entry.pack(pady=5)

# Shift value input
shift_label = ttk.Label(root, text="Enter shift value:")
shift_label.pack(pady=5)
shift_entry = ttk.Entry(root, width=10)
shift_entry.pack(pady=5)

# Mode selection
mode_label = ttk.Label(root, text="Select mode:")
mode_label.pack(pady=5)
mode_combo = ttk.Combobox(root, values=["Encrypt", "Decrypt"])
mode_combo.pack(pady=5)
mode_combo.set("Encrypt")

# Process button
process_button = ttk.Button(root, text="Process", command=process_text)
process_button.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="Result:")
result_label.pack(pady=5)

root.mainloop()
