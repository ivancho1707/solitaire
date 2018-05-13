class Tableu:
    empty_stack_symbol = "[]"

    def __init__(self, deck):
        self._content = [[], [], [], [], [], [], []]
        self._length = 0
        counter = 0
        for i in range(len(self._content)):
            self._content[i] = deck[counter:counter+i+1]
            self._content[i][-1].uncover()
            counter += i+1
        self.length = counter

    def pprint(self):
        for t in self._content:
            if not t:
                print self.empty_stack_symbol,
            else:
                for card in t:
                    card.pprint(False)
                print

    def __len__(self):
        return self._length
