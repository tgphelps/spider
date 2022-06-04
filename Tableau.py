
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
        self.next_deal(deck)

    def next_deal(self, deck: Deck.Deck):
        for p in self.piles:
            p.up_cards.append(deck.deal(1)[0])

    def show(self) -> None:
        print('----' * NUM_PILES)
        self.show_down_cards()
        print('----' * NUM_PILES)
        self.show_up_cards()
        print('----' * NUM_PILES)

    def show_down_cards(self) -> None:
        m = [len(self.piles[i].down_cards) for i in range(NUM_PILES)]
        n = max(m)
        for i in range(n):
            s = ['   X' if x > i else '   ' for x in m]
            print(''.join(s))

    def show_up_cards(self) -> None:
        m = [len(self.piles[i].up_cards) for i in range(NUM_PILES)]
        n = max(m)
        for i in range(n):
            # s = ['  X' if x > i else '   ' for x in m]
            s = ['   ' + Deck.display(self.piles[j].up_cards[i])
                 for j in range(NUM_PILES)]
            print(''.join(s))


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
        print(Deck.display(p.up_cards[0]))

    print()
    print()
    tab.show()
