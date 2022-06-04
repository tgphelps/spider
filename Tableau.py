
import Deck

NUM_PILES = 10
PILES_WITH_5 = 4
PILES_WITH_4 = 6


class Tableau:
    def __init__(self):
        self.piles: list[Pile] = []
        for i in range(NUM_PILES):
            self.piles.append(Pile())

    def initial_deal(self, deck: Deck.Deck):
        for n, p in enumerate(self.piles):
            if n < PILES_WITH_5:
                p.down_cards = deck.deal(5)
            else:
                p.down_cards = deck.deal(4)


class Pile:
    def __init__(self):
        self.down_cards: list[int] = []
        self.up_cards: list[int] = []


if __name__ == '__main__':
    tab = Tableau()
    deck = Deck.Deck(repeatable=True)
    deck.shuffle()
    tab.initial_deal(deck)

    for p in tab.piles:
        print([Deck.display(c) for c in p.down_cards])
