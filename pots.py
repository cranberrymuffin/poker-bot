class Pots:
    def __init__(self, quantity, minimum_bet):
        self.quantity = quantity
        self.minimum_bet = minimum_bet
    
    def addChips(self, chips):
        if chips >= self.minimum_bet:
            self.quantity += chips
        else:
            print ("Invalid bet, play again.")
    
    def payOut(self, total_quantity):
        ##


