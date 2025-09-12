#This file contains the text versions of the Higher or Lower Game
from cards import Card
from cards import Deck

count = 0
attempt = True
valid = True 


d = Deck()
ans = input("Welcome to higher or lower, care to play?? - Y/N \n") 
if ans=="Y" or ans=="y":
    d.initDeck()
    print("Deck was created!!")
    
    while attempt:
        fcard = d.pullACard()
        print(f"The first card is -> {fcard.toString()}")
        val1 = int(d.convertValue(fcard))
           
        while valid:
            choice = input("Is the next card higher, or lower??\n").lower()
            if choice in ("higher","lower"):
                break  # valid, exit inner loop
            else:
                print("Invalid response, try again")
            
        print(f"You chose -> {choice}.")
        sCard = d.pullACard()
        val2 = int(d.convertValue(sCard))
        print(f"Second card is -> {sCard.toString()}")

        match choice:
            case "higher":
                if val1 < val2:
                    count+=1
                    print(f"You were right, it was higher, point earned -> Score:{count}")
                elif val1 == val2:
                    count+=1
                    print(f"Lucky, they were the same, I'll give you a point -> Score:{count}")
                else: 
                    print("Wrong answer, Better luck next time, by bye.")
                    attempt = False

            case "lower":
                if val1 > val2:
                    count+=1
                    print(f"You were right, it was lower, point earned -> Score:{count}")               
                elif val1 == val2:
                    count+=1
                    print(f"Lucky, they were the same, I'll give you a point -> Score:{count}")
                else:
                    print("Wrong answer, Better luck next time, bye bye.")
                    attempt = False
else:
    print("Goodbye, maybe next time.")     
    