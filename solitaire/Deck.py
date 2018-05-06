from solitaire.Card import Card
import random

class Deck:
  def __init__(self):
    self.cards = [Card(x, True) for x in range(52)]
    
  def shuffle(self):
    random.shuffle(self.cards)
    return self.cards