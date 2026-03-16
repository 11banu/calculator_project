import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function when button is clicked
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text,row,col) in buttons:
    if text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    elif text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=equal)
    else:
        btn = tk.Button(root, text=text, width=5, height=2,
                        command=lambda t=text: click(t))
        
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()