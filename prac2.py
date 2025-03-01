import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
root.title("PRAC2")

Label1=tk.Label(root, text="enter your name:")
Entry1=tk.Entry(root)
Label2=tk.Label(root, text="enter your age:")
Entry2=tk.Entry(root)
button=tk.Button(root, text="submit")

Label1.grid(row=0,column=0,padx=10,pady=10)
Entry1.grid(row=0,column=1,padx=10,pady=10)
Label2.grid(row=1,column=0,padx=10,pady=10)
Entry2.grid(row=1,column=1,padx=10,pady=10)
button.grid(row=2, column=0, columnspan=10,pady=10,padx=10)
root.mainloop()