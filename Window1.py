import tkinter as tk
from PIL import ImageTk, Image




root = tk.Tk()
root.title("Main Window")
root.geometry("700x700")

lbl = tk.Label(root, text="Select your customizations below", font=("Times New Roman", 16)) 
lbl.place(x=200, y=10)

photo = tk.PhotoImage(file="C:/Users/lukeh/OneDrive/Pictures/Screenshots 1/0a951bd8d45f60f5258c1e8c47acf769.png")
pic1 = tk.Label(root, image=photo)
pic1.place(x=40, y=30)


root.mainloop()




