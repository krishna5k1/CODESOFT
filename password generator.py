import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()

        self.password_display = tk.Label(root, text="", relief="solid")
        self.password_display.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                messagebox.showerror("Error", "Password length should be a positive integer.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_display.config(text=password)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid positive integer.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
