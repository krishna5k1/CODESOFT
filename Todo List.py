import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# main window
root = tk.Tk()
root.title("To-Do List") 

# Create widgets
task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Submit", command=add_task)
remove_button = tk.Button(root, text="Delete", command=remove_task)
task_listbox = tk.Listbox(root)

# grid layout
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
remove_button.grid(row=0, column=2, padx=10, pady=10)
task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
