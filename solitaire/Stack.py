from abc import ABCMeta, abstractmethod


class Stack:
    __metaclass__ = ABCMeta
    _content = []
    _append_limit = 13
    empty_stack_symbol = "[   ]"

    @abstractmethod
    def validate(self, card_list):
        if len(card_list) > self._append_limit:
            return False
        else:
            raise NotImplementedError

    @abstractmethod
    def ppelement(self): pass

    def pprint(self):
        if not self._content:
            print Stack.empty_stack_symbol,
        else:
            self.ppelement(),

    def append(self, card_list):
        self._content += card_list
