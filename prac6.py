import tkinter as tk 
root=tk.Tk()
root.geometry("200x200")
root.title("prac6")
root.configure(bg="#212121")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
label = tk.Label(root, text="this is label",bg="#ffffff")
# label.pack(expand=True)
label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
btn=tk.Button(root, text="click me",bg="#ffffff")
# btn.pack(expand=True)
btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

root.mainloop()