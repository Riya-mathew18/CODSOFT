import tkinter as tk
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Enter a positive number!")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""
        for i in range(length):
            password += random.choice(characters)
        result_label.config(text=password)
    except ValueError:
        result_label.config(text="Please enter a valid number!")
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")
title_label = tk.Label(window, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)
length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack(pady=5)
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)
window.mainloop()