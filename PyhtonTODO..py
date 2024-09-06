import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do Application")
root.geometry("400x500")

completed_tasks = []
incomplete_tasks = []

def add_task():
    task = task_entry.get()
    if task:
        incomplete_tasks.append(task)
        update_task_display()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def mark_task_complete(task_var, task):
    if task_var.get():
        incomplete_tasks.remove(task)
        completed_tasks.append(task)
        update_task_display()

def update_task_display():
    for widget in incomplete_task_frame.winfo_children():
        widget.destroy()
    completed_task_frame.delete(0, tk.END)

    for task in incomplete_tasks:
        task_var = tk.BooleanVar()
        task_checkbox = tk.Checkbutton(incomplete_task_frame, text=task, variable=task_var, command=lambda t=task_var, task_name=task: mark_task_complete(t, task_name))
        task_checkbox.pack(anchor="w", pady=2)
    for task in completed_tasks:
        completed_task_frame.insert(tk.END, task)

def show_incomplete_tasks():
    incomplete_task_frame.pack()
    completed_task_frame.pack_forget()

def show_completed_tasks():
    completed_task_frame.pack()
    incomplete_task_frame.pack_forget()

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)


incomplete_task_frame = tk.Frame(root)
incomplete_task_frame.pack(pady=10)
completed_task_frame = tk.Listbox(root, width=40, height=10)


incomplete_button = tk.Button(root, text="Incomplete Tasks", command=show_incomplete_tasks)
incomplete_button.pack(pady=5)
completed_button = tk.Button(root, text="Completed Tasks", command=show_completed_tasks)
completed_button.pack(pady=5)

show_incomplete_tasks()
root.mainloop()
