import time


class Stats:

    def __init__(self):
        self.score = 0
        self.moves = 0
        self.timestamp = time.time()

    def pprint(self, board):
        # print game stats
        print "stock: %2d" % len(board.stock),
        print "\t" * 1,
        print "score: %4d" % self.score,
        print "\t" * 1,
        print "moves: %4d" % self.moves,
        print "\t" * 1,
        print "time: %4d" % 0
        print
