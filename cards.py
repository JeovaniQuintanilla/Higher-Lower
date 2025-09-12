import random #get a random num

class Card:

    def __init__(self, face= "", suit= "" ):
        self.face = face
        self.suit = suit

    def setSuit(self, suit):
        self.suit = suit
    
    def setFace(self,face):
        self.face = face

    def getSuit(self):
        return self.suit 
    
    def getFace(self):
        return self.face

    def toString(self):
        return self.face + "_of_" + self.suit
    

class Deck:

    def __init__(self):
        self.faceName = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suitType = ["hearts", "diamonds", "spades", "clubs"]
        self.deck = []

    def initDeck(self):
        for suit in self.suitType:
            for face in self.faceName:
                self.deck.append(Card(face,suit))

    def pullACard(self):
        idx = len(self.deck)
        rand_place = random.randrange(idx)
        card = self.deck.pop(rand_place)

        return card
    
    def convertValue(self, c: Card):
        val = c.getFace()
        if val == "J" or val == "Q" or val == "K":
            return "10"
        elif val == "A":
            return "1"
        else:
            return val
        




#main -- use to test code for file   
s = Card("6","Clubs")
print(s.toString())

#print(len(d.deck)) #test size - 52
#print(d.deck[0].getFace()) #get Face - A
#print(d.deck[0].getSuit()) #get Suit - hearts
#print(len(d.deck)) #test size - 51
#print(d.pullACard())
count = 0
attempt = True


d = Deck()
ans = input("Welcome to higher or lower, care to play?? - Y/N \n") 
if ans=="Y" or ans=="y":
    d.initDeck()
    print("Deck was created!!")
    
    while attempt:
        fcard = d.pullACard()
        print(f"The first card is -> {fcard.toString()}")
        val1 = int(d.convertValue(fcard))

        choice = input("Is the next card higher, or lower??\n").lower()
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
    