
class Card:

    def __init__(self, suit= "", face= ""):
        self.suit = suit
        self.face = face
    

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


    