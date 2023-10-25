import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected_task_index = tasks.curselection()[0]
        tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def update_task():
    try:
        selected_task_index = tasks.curselection()[0]
        updated_task = entry.get()
        tasks.delete(selected_task_index)
        tasks.insert(selected_task_index, updated_task)
        entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("270x270")

# Create an entry widget for task input
entry = tk.Entry(root, width=40)
entry.pack(padx=10,pady=20)

# listbox to display tasks
tasks = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
tasks.pack()

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task,bg='lightblue')
update_button = tk.Button(root, text="Update Task", command=update_task,bg='lightblue')
delete_button = tk.Button(root, text="Delete Task", command=delete_task,bg='lightblue')
add_button.place(x=20,y=230)
update_button.place(x = 90,y=230)
delete_button.place(x=180,y=230)

root.mainloop()
