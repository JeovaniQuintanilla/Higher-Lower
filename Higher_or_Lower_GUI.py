#This file contains the GUI versions of the Higher or Lower Game
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from cards import Card, Deck
import random 

#print("Welcome to the GUI verion of the game")
#Declaring global variables
count = 0
curr = Card()
deck = Deck()

#define objects
def test_function(event):
    num = random.randrange(10)
    label.configure(text=f"{num}")
    print(num)


#--------------------GUI Components
#This is properties for the pane
root = customtkinter.CTk()
root.geometry("800x700")
root.title("Higher & Lower")

#This is the player interaction
label = customtkinter.CTkLabel(root, text="Welcome to Higher or Lower!")
submit = customtkinter.CTkEntry(root, placeholder_text= "Enter your Guess..")

sBtn = customtkinter.CTkButton(root, text="Submit Guess")
sBtn.bind('<Button-1>',test_function)

#Score Area
score = customtkinter.CTkLabel(root, text="Score:")
score.place(x=680, y=625)
#num1 = customtkinter(root)
high_score = customtkinter.CTkLabel(root, text="High-Score:")
high_score.place(x=650, y=600)

label.pack(),submit.pack(),sBtn.pack()



if __name__ == "__main__":
    root.mainloop()