import tkinter as tk
from tkinter import messagebox
from database import *

create_table()

def add():
    if title_entry.get() == "":
        messagebox.showerror("Error", "Title is required")
        return

    add_task(
        title_entry.get(),
        desc_entry.get(),
        status_entry.get(),
        date_entry.get()
    )
    clear()
    load_tasks()

def load_tasks():
    listbox.delete(0, tk.END)
    for task in get_tasks():
        listbox.insert(tk.END, task)

def select(event):
    global selected_task
    try:
        index = listbox.curselection()[0]
        selected_task = listbox.get(index)

        title_entry.delete(0, tk.END)
        title_entry.insert(tk.END, selected_task[1])

        desc_entry.delete(0, tk.END)
        desc_entry.insert(tk.END, selected_task[2])

        status_entry.delete(0, tk.END)
        status_entry.insert(tk.END, selected_task[3])

        date_entry.delete(0, tk.END)
        date_entry.insert(tk.END, selected_task[4])
    except:
        pass

def update():
    try:
        update_task(
            selected_task[0],
            title_entry.get(),
            desc_entry.get(),
            status_entry.get(),
            date_entry.get()
        )
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task")

def delete():
    try:
        delete_task(selected_task[0])
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task")

def clear():
    title_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Task Manager")
window.geometry("500x400")

tk.Label(window, text="Title").pack()
title_entry = tk.Entry(window)
title_entry.pack()

tk.Label(window, text="Description").pack()
desc_entry = tk.Entry(window)
desc_entry.pack()

tk.Label(window, text="Status").pack()
status_entry = tk.Entry(window)
status_entry.pack()

tk.Label(window, text="Due Date").pack()
date_entry = tk.Entry(window)
date_entry.pack()

listbox = tk.Listbox(window)
listbox.pack(fill=tk.BOTH, expand=True)
listbox.bind("<<ListboxSelect>>", select)

tk.Button(window, text="Add Task", command=add).pack()
tk.Button(window, text="Update Task", command=update).pack()
tk.Button(window, text="Delete Task", command=delete).pack()
tk.Button(window, text="Clear Fields", command=clear).pack()

load_tasks()

window.mainloop()