from solitaire.Card import Card
from solitaire.Stack import Stack


class Stock(Stack):

    def __init__(self, deck):
        self._content = deck

    def validate(self, card_list):
        return len(card_list) == self._append_limit

    def ppelement(self):
        print Card.backside_symbol.encode("utf8"),

    def __len__(self):
        return len(self._content)
