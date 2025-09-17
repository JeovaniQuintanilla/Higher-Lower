#This file contains the GUI versions of the Higher or Lower Game
import customtkinter
from tkinter import *
from PIL import Image, ImageTk

print("Welcome to the GUI verion of the game")

root = customtkinter.CTk()
root.geometry("800x700")
root.title("Higher & Lower")

label = customtkinter.CTkLabel(root, text="Welcome to Higher or Lower!")



label.pack()
root.mainloop()