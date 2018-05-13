# -*- coding: utf-8 -*-

from solitaire.Board import Board
from solitaire.Stats import Stats


class Game:
    def __init__(self):
        self.stats = Stats()
        self.board = Board()
  
    def print_board(self):
        self.stats.pprint(self.board)

        self.board.stock.pprint()
        self.board.waste.pprint()
        print "\t" * 3,
        self.board.foundations.pprint()
        print "\n" * 2
        self.board.tableu.pprint()
        print
        print "your move:"
        print