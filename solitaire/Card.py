class Card:
  _suit_symbols = [u"\u2665",u"\u2663", u"\u2666", u"\u2660"]
  _rank_symbols = [" A"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q"," K"]
  backside_symbol = u"\u25A9"
  
  def __init__(self, index, initCovered=False):
    self.rank = (index % 13)
    self.rank_symbol = self._rank_symbols[self.rank]
    self.suit = index / 13
    self.suit_symbol = self._suit_symbols[self.suit]
    self.isCovered = initCovered
    
  def uncover(self):
    self.isCovered = False
  
  
  def pprint(self, breakline=True):
    if not self.isCovered:
      if breakline:
        print self 
      else:
        print self,
    else:
      if breakline:
        Card.backside_symbol.encode("utf8")
      else:
        print Card.backside_symbol.encode("utf8"),
    
  def __str__(self):
    return ("%s%s" % (self.rank_symbol, self.suit_symbol)).encode("utf8")
    
  def __repr__(self):
    return str(self)