
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

#main -- use to test code for file   
s = Card("6","Clubs")
print(s.toString())
    
    