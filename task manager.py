import tkinter as tk
from tkinter import messagebox

# ------------------- Window Setup -------------------
root = tk.Tk()
root.title("Task Management System")
root.geometry("500x550")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

tasks = []

# ------------------- Functions -------------------
def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty")
        return
    tasks.append({"task": task, "status": "Pending"})
    task_entry.delete(0, tk.END)
    refresh_tasks()

def mark_completed():
    try:
        index = task_list.curselection()[0]
        tasks[index]["status"] = "Completed"
        refresh_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

def delete_task():
    try:
        index = task_list.curselection()[0]
        tasks.pop(index)
        refresh_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

def refresh_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        symbol = "✔" if task["status"] == "Completed" else "⏳"
        task_list.insert(tk.END, f"{symbol}  {task['task']}")

# ------------------- Title -------------------
title = tk.Label(
    root,
    text="Task Manager",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
title.pack(pady=20)

# ------------------- Input Frame -------------------
input_frame = tk.Frame(root, bg="#1e1e2f")
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame,
    width=28,
    font=("Segoe UI", 12),
    bd=0
)
task_entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(
    input_frame,
    text="Add",
    font=("Segoe UI", 12, "bold"),
    bg="#4caf50",
    fg="white",
    bd=0,
    width=8,
    command=add_task
)
add_btn.grid(row=0, column=1)

# ------------------- Task List -------------------
list_frame = tk.Frame(root, bg="#1e1e2f")
list_frame.pack(pady=20)

task_list = tk.Listbox(
    list_frame,
    width=40,
    height=12,
    font=("Segoe UI", 12),
    bg="#2a2a40",
    fg="white",
    selectbackground="#4caf50",
    bd=0
)
task_list.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# ------------------- Buttons -------------------
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=15)

complete_btn = tk.Button(
    btn_frame,
    text="Mark Completed",
    font=("Segoe UI", 11),
    bg="#2196f3",
    fg="white",
    bd=0,
    width=15,
    command=mark_completed
)
complete_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(
    btn_frame,
    text="Delete",
    font=("Segoe UI", 11),
    bg="#f44336",
    fg="white",
    bd=0,
    width=15,
    command=delete_task
)
delete_btn.grid(row=0, column=1)

# ------------------- Footer -------------------
footer = tk.Label(
    root,
    text="Python GUI Mini Project",
    font=("Segoe UI", 10),
    bg="#1e1e2f",
    fg="#9e9e9e"
)
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
