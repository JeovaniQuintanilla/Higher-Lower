#This file contains the GUI versions of the Higher or Lower Game
import customtkinter
from tkinter import *
from PIL import Image, ImageTk

print("Welcome to the GUI verion of the game")

root = customtkinter.CTk()
root.geometry("800x700")
root.title("Higher & Lower")


#This is the player interaction
label = customtkinter.CTkLabel(root, text="Welcome to Higher or Lower!")
submit = customtkinter.CTkEntry(root, placeholder_text= "Enter your Guess..")
sBtn = customtkinter.CTkButton(root)

#Score Area



label.pack(),submit.pack(),sBtn.pack()
root.mainloop()