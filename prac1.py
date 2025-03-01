import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
root.title("hello")

#function
def greet():
    user_name=entry.get()
    label_result.config(text=f'hello {user_name}')
    
#creating the element
label=tk.Label(root, text="hello")
entry=tk.Entry(root)
btn=tk.Button(root, text="enter",command=greet) #function add duting the element making
label_result=tk.Label(root, text="")

#display format
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
btn.grid(row=1, column=0, columnspan=2, pady=10)
label_result.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()