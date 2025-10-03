#This file contains the GUI versions of the Higher or Lower Game
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
import random
from cards import Card, Deck 
from pathlib import Path

#print("Welcome to the GUI verion of the game")
#Declaring global variables



class Higherorlower(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.curr = Card()
        self.deck = Deck()
        self.deck.initDeck()
        self.curr = self.deck.pullACard()
        print(self.curr.toString())
        self.createGameLayout()

    def confirmInput(self):
        self.ans = self.submitField.get().lower()
        print(self.ans)
        if self.ans != "lower" and self.ans != "higher":
            self.directionslabel.configure(text="Invalid Guess Input, type either higher or lower.")
        else:
            self.directionslabel.configure(text="Yay you can read")

    def createGameLayout(self):
        self.highscore = 0
        self.count = 0
        
        self.geometry("800x700")
        self.title("Higher & Lower")        
        self.directionslabel = customtkinter.CTkLabel(self, text="Welcome to Higher or Lower!")
        self.directionslabel.pack()
        
        self.submitField = customtkinter.CTkEntry(self, placeholder_text= "Enter your Guess..")
        self.submitField.pack()

        self.sBtn = customtkinter.CTkButton(self, text="Submit Guess")
        self.sBtn.bind('<Button-1>',lambda e: self.confirmInput())
        self.sBtn.pack()

        self.scoreLabel = customtkinter.CTkLabel(self, text="Score:")
        self.scoreLabel.place(x=680, y=625)
        self.high_scoreLabel = customtkinter.CTkLabel(self, text="High-Score:")
        self.high_scoreLabel.place(x=650, y=600)


if __name__ == "__main__":
    root = Higherorlower()
    root.mainloop()