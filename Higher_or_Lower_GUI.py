#This file contains the GUI versions of the Higher or Lower Game
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from cards import Card, Deck 
from pathlib import Path
import os

#print("Welcome to the GUI verion of the game")
#Declaring global variables


CARDS_FOLDER = "Higher-Lower/playingCards"

class Higherorlower(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.count = 0
        self.geometry("800x700")
        self.title("Higher & Lower")

        self.curr = Card()
        self.deck = Deck()
        self.sCard = None
        self.ans = " "

        self.deck.initDeck()
        self.curr = self.deck.pullACard()
        print(f"curr card: {self.curr.toString()}")
        self.createGameLayout()

        self.directionslabel.configure(text=f"The first card is {self.curr.toString().replace("_", " ")}, is the next one Higher or Lower??")
        self.card1.configure(image=self.img1)
        self.card2.configure(image=self.boc)
        self.sBtn.bind('<Button-1>', lambda e: self.confirmInput())

    def confirmInput(self, event=None):
        self.ans = self.submitField.get().lower()
        print(self.ans)
        #self.submitField.configure(state="disabled")
        #self.sBtn.configure(state="disabled")
        if self.ans != "lower" and self.ans != "higher":
            self.directionslabel.configure(text="Invalid Guess Input, type either higher or lower.")
        else:
            self.getSecondCard()
            self.after(2000, self.updateGame)

        
    def updateGame(self):
        print("Switching cards now")
        bool1 = self.compareCards(self.curr,self.sCard,self.ans)

        if (bool1==True):
            self.switchCards()
            self.incScore()
            self.directionslabel.configure(text=f"The first card is {self.curr.toString().replace("_", " ")}, is the next one Higher or Lower")
            print("score updated.")
        else:
            self.resetScore()
            self.directionslabel.configure(text=f"Wrong try again. Is the Second Card Higher or Lower?")
            self.card2.configure(image=self.boc)
            print("score reset.")

    def getSecondCard(self):
        self.sCard = self.deck.pullACard()
        print(f"SecondCard: {self.sCard.toString()}")
        self.img2 = customtkinter.CTkImage(
                light_image=Image.open(Path(CARDS_FOLDER) / f"{self.sCard.toString()}.png"),
                dark_image=Image.open(Path(CARDS_FOLDER) / f"{self.sCard.toString()}.png"),
                size=(100, 145)
            )
        self.directionslabel.configure(text=f"Second Card is {self.sCard.toString()}")
        self.card2.configure(image=self.img2)
        
    def switchCards(self):
        self.curr = self.sCard
        self.img1 = self.img2
        self.card1.configure(image=self.img1)
        self.card2.configure(image=self.boc)

    def compareCards(self,  x: Card,  y: Card, ans):
        val1 = int(self.deck.convertValue(x))
        val2 = int(self.deck.convertValue(y))
        flag = False

        if val1 == val2:
            return True
        else:
            match (ans):
                case "higher":
                    if val1 < val2:
                        flag = True
                
                case "lower":
                    if val1 > val2:
                        flag = True
            print(flag)
            return flag
    
    def incScore(self):
        self.count+=1
        self.scoreLabel.configure(text=f"Score: {self.count}")
        if self.count > self.high_score:
            self.high_score = self.count
            self.high_scoreLabel.configure(text=f"High Score: {self.high_score}")
    
    def resetScore(self):
        self.count=0
        self.scoreLabel.configure(text=f"Score: {self.count}")

    def createGameLayout(self):
        #Image of first Card
        self.img1 = customtkinter.CTkImage(
            light_image=Image.open(Path(CARDS_FOLDER) / f"{self.curr.toString()}.png"),
            dark_image=Image.open(Path(CARDS_FOLDER) / f'{self.curr.toString()}.png'),
            size=(100, 145)
        )
         #Back of Card
        self.boc = customtkinter.CTkImage(
            light_image=Image.open("Higher-Lower/Back_of_card.png"),
            dark_image=Image.open("Higher-Lower/Back_of_card.png"),
            size=(100, 145)
        )
       
        #card 1 place
        self.card1 = customtkinter.CTkLabel(self, text="", bg_color="white", image=None)
        self.card1.place(x=245, y=160)
        #Card 2 place
        self.card2 = customtkinter.CTkLabel(self, text="", bg_color="white", image=None)
        self.card2.place(x=455.5, y=160)
             
        self.directionslabel = customtkinter.CTkLabel(self, text="Welcome to Higher or Lower!")
        self.directionslabel.pack()
        
        self.submitField = customtkinter.CTkEntry(self, placeholder_text= "Enter your Guess..")
        self.submitField.pack()

        self.sBtn = customtkinter.CTkButton(self, text="Submit Guess")
        self.sBtn.pack()

        self.scoreLabel = customtkinter.CTkLabel(self, text=f"Score: {self.count}")
        self.scoreLabel.place(x=680, y=625)
        self.high_scoreLabel = customtkinter.CTkLabel(self, text=f"High-Score: {self.high_score}")
        self.high_scoreLabel.place(x=650, y=600)


if __name__ == "__main__":
    root = Higherorlower()
    root.mainloop()