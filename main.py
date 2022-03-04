import tkinter as tk


root = tk.Tk()

root.title('Test')
root.geometry('500x500')

scale = tk.Scale(root, resolution=0.1, from_=0.1, to=5.0)
scale.pack()

root.mainloop()

print('DBG')

