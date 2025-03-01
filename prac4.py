import tkinter as tk
root=tk.Tk()
root.geometry("400x300")
root.title("prac4")

def new_window():
    new=tk.Toplevel(root)
    new.title("new window")
    new.geometry("200x200")
    label=tk.Label(new, text="new window opened")
    label.pack(pady=20,padx=20)
    
label=tk.Label(root, text="Click the button for new window")
label.pack(padx=20,pady=20)
button=tk.Button(root, text="click me", command=new_window)
button.pack(padx=20, pady=20)
root.mainloop()