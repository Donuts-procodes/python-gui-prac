import tkinter as tk
root=tk.Tk()
root.geometry("300x300")
root.title("prac5")

frame=tk.Frame( root, padx=10, pady=10,relief="ridge",borderwidth=5)
frame.pack()

label=tk.Label(frame, text="this is inside the frame")
label.pack()
btn=tk.Button(frame, text="Click me")
btn.pack()

root.mainloop()