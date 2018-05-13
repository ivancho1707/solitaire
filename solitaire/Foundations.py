from solitaire.Stack import Stack


class Foundations():
    class Foundation(Stack):
        @staticmethod
        def validate_harmonics(card_list):
            return True  # TODO

        def validate(self, card_list):
            if len(card_list) > self._append_limit or not self.validate_harmonics(self._content + card_list):
                return False
            return True

        def ppelement(self):
            print "[%s]" % self._content[0]

    def pprint(self):
        for f in self._content:
            f.pprint()

    def __init__(self):
        self._content = [self.Foundation(), self.Foundation(), self.Foundation(), self.Foundation()]
