import tkinter as tk
root=tk.Tk()
root.geometry("200x100")
root.title("prac3")

def show_messege():
    label.config(text="Button Clicked!!!")

label=tk.Label(root, text="Click the button")
label.pack(pady=10)
button=tk.Button(root, text="enter", command=show_messege)
button.pack(pady=10)

root.mainloop()