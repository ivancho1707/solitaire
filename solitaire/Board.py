from solitaire.Deck import Deck
from solitaire.Waste import Waste
from solitaire.Stock import Stock
from solitaire.Tableu import Tableu
from solitaire.Foundations import Foundations


class Board:

    def __init__(self):
        deck = Deck().shuffle()
        self.waste = Waste()
        self.foundations = Foundations()
        self.tableu = Tableu(deck)
        self.stock = Stock(deck[len(self.tableu):])
