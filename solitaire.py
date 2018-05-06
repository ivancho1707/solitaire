from solitaire.Deck import Deck

def main():
    deck = Deck().shuffle()
    for card in deck:
        print card

if __name__ == "__main__":
    main()