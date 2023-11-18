import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_tasks_display()

def delete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks.pop(index)
        update_tasks_display()
    except IndexError:
        pass

def update_tasks_display():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List")

tasks = []

# Set background color for the main window
root.configure(bg="lightgray")

task_frame = tk.Frame(root, bg="lightgray")  # Set background color for the task frame
task_frame.pack(padx=10, pady=10)

tasks_listbox = tk.Listbox(task_frame, width=50, height=10, bd=0, bg="white")  # Set background color for the listbox
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

add_button = tk.Button(root, text="Add Task", width=48, command=add_task, bg="lightblue")  # Set background color for the button
add_button.pack(padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Task", width=48, command=delete_task, bg="salmon")  # Set background color for the button
delete_button.pack(padx=10, pady=5)

root.mainloop()
