import tkinter as tk
from tkinter import messagebox
from tasks import TaskManager

# Initialize Tkinter
root = tk.Tk()
root.title("To-Do List")

task_manager = TaskManager()

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_manager.add_task(task)
        update_listbox()
        task_entry.delete(0, tk.END)

# Function to remove a selected task
def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_manager.remove_task(selected_task[0])
        update_listbox()

# Function to update listbox
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in task_manager.get_tasks():
        task_listbox.insert(tk.END, task)

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack()

root.mainloop()

