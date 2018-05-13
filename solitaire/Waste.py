from solitaire.Stack import Stack


class Waste(Stack):
    _append_limit = 1

    def validate(self, card_list):
        return len(card_list) == self._append_limit

    def ppelement(self):
        print "[%s]" % self._content[0]