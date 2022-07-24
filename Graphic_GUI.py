from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title('GUI Solidworks Analysis Data')
root.geometry('650x500')
root.resizable(False, False)
my_tree = ttk.Treeview(root)

list1 = [[i for i in range(4)] for i in range(4)]
list2 = [[i for i in range(4,8)] for i in range(4)]

def handle_click(event):
    if my_tree.identify_region(event.x, event.y) == "separator":
        return "break"

# Define columns
my_tree['columns'] = ('Frequency', 'Mass X', 'Mass Y', 'Mass Z')

# Formate our columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Frequency', anchor=CENTER, width=120)
my_tree.column("Mass X", anchor=CENTER, width=120)
my_tree.column("Mass Y", anchor=CENTER, width=120)
my_tree.column("Mass Z", anchor=CENTER, width=120)

my_tree.heading("#0", text='', anchor=CENTER)
my_tree.heading("Frequency", text='Frequency', anchor=CENTER)
my_tree.heading("Mass X", text='Mass X', anchor=CENTER)
my_tree.heading("Mass Y", text='Mass Y', anchor=CENTER)
my_tree.heading("Mass Z", text='Mass Z', anchor=CENTER)

my_tree.pack(pady=20, fill='y')

#Set entry
lbl = Label(root, text="Percent mass filter")
lbl.place(relx=0.1, rely=0.8, relwidth=0.15, relheight=0.04)

entry = tk.Entry(bg='white', font=1)
entry.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.04)

#Functions


#button add
button = tk.Button(text='Zastosuj', font=('Segoe UI', 10), command= lambda: print(1))
button.place(relx=0.3, rely=0.85, relheight=0.05, relwidth=0.2)

#button add
button_2 = tk.Button(text='Show all', font=('Segoe UI', 10), command= lambda: None)
button_2.place(relx=0.5, rely=0.85, relheight=0.05, relwidth=0.2)


my_tree.bind('<Button-1>', handle_click)
root.mainloop()