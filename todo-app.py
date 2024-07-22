import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("To-Do Application")
root.geometry("700x500")

current_directory = r'C:\Users\143kd\OneDrive\Documents\tkinter'

deleteImage = Image.open(os.path.join(current_directory, "delete_icon.png"))
editImage = Image.open(os.path.join(current_directory, "edit_icon.png"))

deleteImage = deleteImage.resize((20, 20))
editImage = editImage.resize((20, 20))

deleteIcon = ImageTk.PhotoImage(deleteImage)
editIcon = ImageTk.PhotoImage(editImage)

inputFrame  = tk.Frame(root)
inputFrame.pack(pady=20)

myEntry = tk.Entry(inputFrame, font=("Arial", 16), width=30)
myEntry.grid(row=0, column=0, padx=5)

def print_task(event):
    task = myEntry.get()
    if task:
        add_task()
    return "break"

myEntry.bind('<Return>', print_task)

def add_task():
    task = myEntry.get()
    
    taskFrame = tk.Frame(taskListFrame)
    taskFrame.pack(fill=tk.X, pady=10)

    taskFrame.grid_columnconfigure(0, weight=1)

    taskText = tk.Text(taskFrame, wrap="none", width=40, height=1, font=("Arial", 16))
    taskText.insert(tk.END, task)
    taskText.config(state=tk.DISABLED)
    taskText.grid(row=0, column=0, padx=5)

    scrollbar = tk.Scrollbar(taskFrame, orient="horizontal", command=taskText.xview)
    scrollbar.grid(row=0, column=1)

    taskText.config(xscrollcommand=scrollbar.set)

    deleteButton = tk.Button(taskFrame, image=deleteIcon, command=lambda: delete_task(taskFrame))
    deleteButton.grid(row=0, column=1 , padx=(5, 10))

    editButton = tk.Button(taskFrame, image=editIcon, command=lambda: edit_task(taskText))
    editButton.grid(row=0, column=2, padx=(5, 10))

    myEntry.delete(0, tk.END)

def delete_task(taskFrame):
    taskFrame.destroy()

def edit_task(taskText):

    def save_changes(event):
        updated_task = taskText.get("1.0", tk.END).strip()
        if updated_task:
            taskText.config(state=tk.DISABLED)
        return "break"
    
    taskText.config(state=tk.NORMAL)
    taskText.bind('<Return>', save_changes)

addButton = tk.Button(inputFrame, text="Add Task", command=add_task, bg='#007acc', fg='#ffffff', font=("Arial", 14, "bold"), padx=5, pady=2, relief="raised",bd=0, activebackground="#005f99", activeforeground="#ffffff")
addButton.grid(row=0, column=1, padx=5)

taskListFrame = tk.Frame(root)
taskListFrame.pack(pady=10)

'''def printTask(event):
    task = myEntry.get()
    print(task)

task = myEntry.get()
myEntry.bind('<KeyRelease>', printTask)'''


root.mainloop()