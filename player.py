class Player:
   def __init__(self, discord_id, card1, card2, chips):
      self.discord_id = discord_id
      self.card1 = card1
      self.card2 = card2
      self.chips = chips
      self.isActive = True
      
   def dealHand(self, card1, card2):
      self.card1 = card1
      self.card2 = card2

   def playTurn(self, action, minimumBet):
      if(action == call):
         
      '''
         await:
            !call
            !check
            !fold foldQuantity
         from discord_id

         if(fold):
            isActive = false
         
         if(check):
            addChips(0)

         if(call):
            addChips(call)
            chips = chips - foldQuantity
      '''