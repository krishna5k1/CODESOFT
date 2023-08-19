import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        if float(second_number) != 0:
            entry.insert(0, f_num / float(second_number))
        else:
            entry.insert(0, "Error")

#  main window
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons on the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: button_click(b) if b.isdigit() or b == '.' else button_clear() if b == 'C' else button_equal() if b == '=' else button_add() if b == '+' else button_subtract() if b == '-' else button_multiply() if b == '*' else button_divide() if b == '/' else None).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
