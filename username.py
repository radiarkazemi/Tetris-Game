import tkinter as tk
from tkinter import messagebox

username = ""


def show_name():
    global username
    username = entry.get()
    if username:
        root.destroy()
    else:
        messagebox.showerror("Error", "Please enter your name")


root = tk.Tk()
root.geometry("400x200")
root.config(bg="#1C1C1C")
root.title("Player Name")

label = tk.Label(root, text="Enter Your Name", font=("TkDefaultFont", 16), bg="#1C1C1C", fg="#FFFFFF")
label.pack(pady=20)

entry = tk.Entry(root, font=("TkDefaultFont", 14))
entry.pack(pady=20)

button = tk.Button(root, text="Submit", font=("TkDefaultFont", 14), bg="#454545", fg="#FFFFFF", command=show_name)
button.pack(pady=20)

root.mainloop()

print("Username:", username)
